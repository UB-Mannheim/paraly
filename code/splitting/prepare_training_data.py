import pandas as pd
from sklearn.model_selection import train_test_split

# Adjust the labels to handle both "cf" and "fc" annotations
def generate_labels(label):
    if pd.isna(label):  # Handle NaN values
        return ""
    if "cf" in label:
        return "__label__figuratif __label__concret"
    elif "fc" in label:
        return "__label__concret __label__figuratif"
    elif "f" in label:
        return "__label__figuratif"
    elif "c" in label:
        return "__label__concret"
    else:
        return ""

# List of file paths and sheet names
files = [
    {'file_path': '../data/annotated/01 AnnotXVIII_gesamt.xlsx', 'sheet_name': 'merge'},
    {'file_path': '../data/annotated/02_AnnotXX_gesamt.xlsx', 'sheet_name': 'merge'},
    {'file_path': '../data/annotated/AnnotatXIX_sdewey80.xlsx', 'sheet_name': 'merge'}
]

# Initialize an empty DataFrame for storing combined data
combined_df = pd.DataFrame()

# Loop through each file and process the data
for file in files:
    df = pd.read_excel(file['file_path'], sheet_name=file['sheet_name'])
    df['text'] = df['Pre'].astype(str) + ' ' + df['Match'].astype(str) + ' ' + df['Post'].astype(str)
    df['labels'] = df['figuratif (f) ou concret (c)'].apply(generate_labels)
    # Add filename column
    df['filename'] = file['file_path'].split('/')[-1]
    # Keep original index
    df['index'] = df.index
    # Select columns including filename and index
    fasttext_df = df[['labels', 'text', 'filename', 'index']]
    #fasttext_df = df[['labels', 'text']]

    # Append to the combined dataframe
    combined_df = pd.concat([combined_df, fasttext_df])

# Create a column that combines all the labels for stratified splitting
combined_df['label_key'] = combined_df['labels'].apply(lambda x: ' '.join(sorted(x.split())))
combined_df = combined_df[combined_df['labels'].str.strip() != ""]

# Find the labels that occur more than once for stratified splitting
label_counts = combined_df['label_key'].value_counts()
stratified_labels = label_counts[label_counts > 1].index
non_stratified_labels = label_counts[label_counts == 1].index

# Split the data into stratified and non-stratified sets
stratified_df = combined_df[combined_df['label_key'].isin(stratified_labels)]
non_stratified_df = combined_df[combined_df['label_key'].isin(non_stratified_labels)]

# Stratified split: Train (80%), Test (10%), Dev (10%)
train_stratified, temp_stratified = train_test_split(stratified_df, test_size=0.3, stratify=stratified_df['label_key'], random_state=42)
dev_stratified, test_stratified = train_test_split(temp_stratified, test_size=0.5, stratify=temp_stratified['label_key'], random_state=42)

# Handle non-stratified labels with only one sample
train_non_stratified = non_stratified_df  # Assign them directly to the training set (since they can't be split)

# Combine the stratified and non-stratified splits
train_df = pd.concat([train_stratified, train_non_stratified])
dev_df = pd.concat([dev_stratified])
test_df = pd.concat([test_stratified])

# Function to save a dataframe without using to_csv and avoiding quotation marks
def save_dataframe_to_txt(df, file_path):
    with open(file_path, 'w') as f:
        for row in df.itertuples(index=False, name=None):  # Convert each row to a tuple without the index
            row_str = ' '.join(map(str, row))  # Join the tuple values with space as separator
            f.write(row_str + '\n')  # Write the row string and add a newline


# Drop the 'label_key' column as it's not needed anymore
train_df = train_df.drop(columns=['label_key', 'filename', 'index'])
dev_df = dev_df.drop(columns=['label_key', 'filename', 'index'])
test_df = test_df.drop(columns=['label_key', 'filename', 'index'])

# Save the splits to respective files using the custom save function
save_dataframe_to_txt(train_df, './train_fasttext_dataset.txt')
save_dataframe_to_txt(dev_df, './dev_fasttext_dataset.txt')
save_dataframe_to_txt(test_df, './test_fasttext_dataset.txt')

# Function to clean and print descriptive statistics for a DataFrame
def print_split_statistics(df, split_name):
    print(f"--- {split_name} ---")
    print(f"Number of samples: {len(df)}")

    # Clean up the labels by removing the "__label__" prefix
    df_cleaned = df.copy()
    df_cleaned['cleaned_labels'] = df_cleaned['labels'].apply(lambda x: ' '.join([label.replace("__label__", "") for label in x.split()]))

    label_counts = df_cleaned['cleaned_labels'].value_counts()
    print("Label distribution:")
    print(label_counts)
    print("\n")

# Print statistics for each split
print_split_statistics(train_df, "Training Set")
print_split_statistics(dev_df, "Development Set")
print_split_statistics(test_df, "Test Set")

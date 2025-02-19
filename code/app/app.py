import gradio as gr
from flair.models import TextClassifier
from flair.data import Sentence

# Load the classifier model
classifier = TextClassifier.load('../../data/model/paraly_camembert_large_multilabel.pt')

# Convert French label to English label
def convert(label):
    if label == "figuratif":
        return "figurative"
    if label == "concret":
        return "concrete"

# Define the prediction function
def predict(input_text):
    sentence = Sentence(input_text)
    classifier.predict(sentence)

    # Extract the label and confidence into a dictionary format
    labels = {convert(label.value): label.score for label in sentence.labels}

    return labels

# Create Gradio Interface for text classification
app = gr.Interface(
    fn=predict,  # the function that processes the input
    inputs=gr.Textbox(label="Input Text"),  # the input field (textbox)
    outputs=gr.Label(label="Predicted Labels"),  # the output display (label)
    title="Paraly-Classifier",  # title of the app
    description="This app classifies text into relevant categories.",  # app description
    examples=["Souvent, les contrôles trop nombreux ne font que ralentir et paralyser les activités.",
              "Foudroyé par une catastrophe invraisemblable, inouïe, qui l'atteignait en plein bonheur, son cerveau avait été pour un moment frappé de paralysie",
              "Pharaon était paralytique général"]  # example inputs
)

if __name__ == "__main__":
    app.launch()

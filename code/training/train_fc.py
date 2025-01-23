from flair.data import Corpus
from flair.datasets import ClassificationCorpus
from flair.embeddings import TransformerDocumentEmbeddings
from flair.models import TextClassifier
from flair.trainers import ModelTrainer

modelname = 'camembert' # ['flaubert', 'camembert', 'bert_base']
mode = 'multi' # ['single', 'multi']
models = {'flaubert': 'flaubert/flaubert_base_cased',
          'camembert': 'camembert/camembert-large',
          'bert_base': 'bert-base-multilingual-uncased'}
label_type = "label"

corpus: Corpus = ClassificationCorpus(data_folder="../data/training/",
                                      train_file=mode + 'label_train_fasttext_dataset.txt',
                                      dev_file=mode + 'label_dev_fasttext_dataset.txt',
                                      test_file=mode + 'label_test_fasttext_dataset.txt',
                                      label_type=label_type)

label_dict = corpus.make_label_dictionary(label_type=label_type)
document_embeddings = TransformerDocumentEmbeddings(models[modelname], fine_tune=True)

if mode=='multi':
    clf = TextClassifier(document_embeddings, label_dictionary=label_dict, label_type=label_type, multi_label_threshold=0.4, multi_label=True)
elif mode=='single':
    clf = TextClassifier(document_embeddings, label_dictionary=label_dict, label_type=label_type, multi_label=False)

trainer = ModelTrainer(clf, corpus)

if modelname == 'flaubert':
    trainer.train('../data/model/paraly_flaubert_base_cased_' + mode + 'label/',
                 learning_rate=8e-3,
                 mini_batch_size=1,
                 max_epochs=10)
if modelname == 'camembert':
    trainer.train('../data/model/paraly_camembert_large_' + mode + 'label/',
                  learning_rate=8e-3,
                  mini_batch_size=1,
                  max_epochs=10)
if modelname == 'bert_base':
    trainer.train('../data/model/paraly_bert_base_multilingual_uncased_' + mode + 'label/',
                  learning_rate=8e-3,
                  mini_batch_size=1,
                  max_epochs=10)

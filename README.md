# Paraly: An (annotated) dataset for exploring the concept of paralysis (fr. ‘paralysie’) in a digital corpus of French Literature

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Open Code](https://badgen.net/static/open/code/green)](https://github.com/UB-Mannheim/paraly/tree/main/code)
[![Open Data](https://badgen.net/static/open/data/green)](https://github.com/UB-Mannheim/paraly/tree/main/data)
[![Open Science](https://badgen.net/static/open/science/green)](https://en.wikipedia.org/wiki/Open_science)

## Table of contents

* [Structure](#structure)
* [Collection](#collection)
* [Annotation](#annotation)
* [Model](#model)
* [App](#app)
* [License](#license)

## Structure

```
paraly/
├── docs/
│   └── paraly_annotation_guidelines.pdf
├── data/
│   ├── training/
│   │   ├── train_fasttext_dataset.txt
│   │   ├── test_fasttext_dataset.txt
│   │   └── dev_fasttext_dataset.txt
│   ├── model/
│   │   ├── training.log
│   │   ├── test.tsv
│   │   ├── paraly_camembert_large_multilabel.pt
│   │   ├── loss.tsv
│   │   └── dev.tsv
│   ├── errors/
│   │   └── all_metadata_errors.csv
│   ├── corpus/
│   │   ├── 20_paraly_metadata.csv
│   │   ├── 20_paraly_data_TEI.xml/
│   │   ├── 20_paraly_corpus.cec6
│   │   ├── 19_paraly_metadata.csv
│   │   ├── 19_paraly_data_TEI.xml/
│   │   ├── 19_paraly_corpus.cec6
│   │   ├── 18_paraly_metadata.csv
│   │   ├── 18_paraly_data_TEI.xml/
│   │   └── 18_paraly_corpus.cec6
│   └── annotations/
│       ├── 20_paraly_annotations_v1.xlsx
│       ├── 20_paraly_annotations_v1.csv
│       ├── 19_paraly_annotations_v1.xlsx
│       ├── 19_paraly_annotations_v1.csv
│       ├── 18_paraly_annotations_v1.xlsx
│       └── 18_paraly_annotations_v1.csv
├── code/
│   ├── training/
│   │   ├── train_fc.py
│   │   └── README_training.md
│   ├── splitting/
│   │   ├── prepare_training_data.py
│   │   └── README_splitting.md
│   ├── merging/
│   │   ├── README_merging.md
│   │   └── Merge.ipynb
│   ├── extraction/
│   │   ├── query.txt
│   │   ├── Starten.bat
│   │   ├── Skript.cecs
│   │   └── README_extraction.md
│   ├── collection/
│   │   ├── get_metadata_for_corpus.ipynb
│   │   ├── get_metadata_for_all_books.ipynb
│   │   ├── get_OCRed_books_from_gallica.ipynb
│   │   └── comment_metadata_in_html_files.ipynb
│   └── app/
│       └── app.py
├── README.md
└── LICENSE.md
```

## Collection

The whole digital collection for various centuries is at https://gallica.bnf.fr/html/und/litteratures/les-classiques-de-la-litterature-acces-par-periode?mode=desktop. Our focus is on the following collections:

* https://gallica.bnf.fr/html/und/litteratures/les-classiques-de-la-litterature-du-xviiie-siecle?mode=desktop
* https://gallica.bnf.fr/html/und/litteratures/les-classiques-de-la-litterature-du-xixe-siecle?mode=desktop
* https://gallica.bnf.fr/html/und/litteratures/les-classiques-de-la-litterature-du-xxe-siecle?mode=desktop

The OCR-ed books and their metadata were downloaded using the scripts in `./code/collection/`.

## Annotation

The annotated data located in `./data/annotations/` was labeled as "c" (concrete), "f" (figurative), and “cf” (an “inter-“category).

## Model

The multilabel classifier [paraly_camembert_large_multilabel](https://huggingface.co/shigapov/paraly_camembert_large_multilabel/tree/main) was trained using flair-library with a script in `./code/training/` and is openly available at Hugging Face. 

## App

The app for using the classifier is openly available via [Hugging Face Spaces](https://huggingface.co/spaces/shigapov/paraly).

## License

Unless stated otherwise, this work is licensed as follows:  

- **MIT License** for code  
- **CC0** for files containing metadata only  
- **[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)** for all other content  


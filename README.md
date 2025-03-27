# PDF Similarity Checker

This project is a Python script that compares the textual content of a specified PDF file against a collection of text files and PDFs in a given directory. It calculates the similarity using TF-IDF vectorization and cosine similarity, and outputs only those comparisons where the similarity is greater than 50%.

## Features

- Extracts text from PDF and TXT files.
- Calculates similarity scores using TF-IDF and cosine similarity.
- Outputs similarity scores greater than 50%.

## Requirements

- Python 3.x
- Required libraries:
  - `PyPDF2`
  - `scikit-learn`

You can install the required libraries using pip:

```bash
pip install PyPDF2 scikit-learn
```
===================================================================
## Usage
Run the script.
When prompted, enter the full path of the PDF file you want to analyze.
The script will process the input PDF and compare it with the text files in the specified folder, printing the similarity scores.

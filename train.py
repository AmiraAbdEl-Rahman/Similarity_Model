import os
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to read all files from a folder
def read_files_from_folder(folder_path):
    texts = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.endswith('.pdf'):
            texts.append(extract_text_from_pdf(file_path))
        elif filename.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as f:
                texts.append(f.read())
    return texts

# Take input PDF path from the user
input_pdf = input("Enter the path to the input PDF file: ")
folder_path = "C:/Users/Data/Desktop/doc"  

# Extract text from the input PDF
input_text = extract_text_from_pdf(input_pdf)

# Read all texts from the specified folder
archive_texts = read_files_from_folder(folder_path)

# Calculate similarity using TF-IDF vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([input_text] + archive_texts)
similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])

# Print similarity scores greater than 50%
similarity_scores = [(i + 1, score) for i, score in enumerate(similarity_matrix[0]) if score > 0.5]
for file_index, score in similarity_scores:
    print(f"Similarity between {input_pdf} and File {file_index}: {score:.2f}")
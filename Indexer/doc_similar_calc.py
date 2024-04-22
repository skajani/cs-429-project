import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

def preprocess_text(text):
    return text

def load_documents(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        documents = [preprocess_text(doc.get('text_content', '')) for doc in data]
    return documents

def save_pickle(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_pickle(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

def calculate_similarity(tfidf_matrix):
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix

directory = "./crawled_docs"
json_file = "output.json"

# Load and preprocess documents
documents = load_documents(json_file)

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Save TF-IDF matrix in pickle format
save_pickle(tfidf_matrix, 'tfidf_matrix.pkl')

# Calculate similarity matrix
similarity_matrix = calculate_similarity(tfidf_matrix)

# Save similarity matrix in pickle format
save_pickle(similarity_matrix, 'similarity_matrix.pkl')

# Create a dictionary mapping terms to their tf-idf vectors
inverted_index = {term: tfidf_matrix.getcol(idx).toarray().ravel().tolist() for term, idx in vectorizer.vocabulary_.items()}

# Save the inverted index in pickle format
save_pickle(inverted_index, 'inverted_index.pkl')

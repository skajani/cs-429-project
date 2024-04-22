import pickle

def display_inverted_index(inverted_index, limit=50):
    print("Inverted Index:")
    for i, (term, vector) in enumerate(inverted_index.items()):
        if i >= limit:
            break
        print(f"{term}: {vector}")

def display_similarity_matrix(similarity_matrix, limit=10):
    print("Similarity Matrix:")
    for i, row in enumerate(similarity_matrix):
        if i >= limit:
            break
        print(f"Row {i+1}: {row[:limit]}")  

# Load the inverted index from the pickle file
with open('inverted_index.pkl', 'rb') as f:
    inverted_index = pickle.load(f)

# Display the inverted index
display_inverted_index(inverted_index)

# Load the similarity matrix from the pickle file
with open('similarity_matrix.pkl', 'rb') as f:
    similarity_matrix = pickle.load(f)

# Display the similarity matrix
display_similarity_matrix(similarity_matrix)
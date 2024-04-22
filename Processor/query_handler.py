from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

def load_data():
    with open('inverted_index.pkl', 'rb') as f:
        inverted_index = pickle.load(f)
    with open('similarity_matrix.pkl', 'rb') as f:
        similarity_matrix = pickle.load(f)
    return inverted_index, similarity_matrix

def process_query(query, inverted_index, similarity_matrix, k=10):
    query_vector = np.array([inverted_index.get(word, [0]*len(similarity_matrix)) for word in query.split()]).mean(axis=0)
    query_vector /= np.linalg.norm(query_vector)  # Normalize query vector
    
    similarities = np.dot(similarity_matrix, query_vector)
    
    k_indicies = similarities.argsort()[-k:]
    k_similar = similarities[k_indicies]

    return [{'document': int(i), 'similarity score': float(s)} for i, s in zip(k_indicies, k_similar)]

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({'error': 'No query provided'}), 400

    query = data['query']
    k = data.get('k', 10)  

    if not isinstance(query, str) or not query.strip():
        return jsonify({'error': 'Empty or non-string query'}), 400
    if not isinstance(k, int) or k < 1:
        return jsonify({'error': 'Invalid k value (must be a positive integer)'}), 400

    inverted_index, similarity_matrix = load_data()
    results = process_query(query, inverted_index, similarity_matrix, k)
    
    response = {'query': query, 'results': results}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, load_dotenv=False)
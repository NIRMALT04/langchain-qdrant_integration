from flask import Flask, request, jsonify
from main import process_query

app = Flask(__name__)

# API endpoint to process queries
@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    query = data.get('query')

    if not query:
        return jsonify({"error": "Query is required"}), 400

    try:
        # Call the main.py function to process the query
        result, score = process_query(query)
        return jsonify({"answer": result, "score": score})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)

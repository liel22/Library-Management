# File: search_book_service.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

# Initialize Flask app
app = Flask(__name__)
CORS(app)
try:
    MONGO_URI = "mongodb+srv://matank222:ElzWhd3CUam4K8iw@library.l5ntd.mongodb.net/?retryWrites=true&w=majority&appName=library"
    client = MongoClient(MONGO_URI)
    client.admin.command('ping')  # Check connection
    print("Connected to MongoDB successfully")
except errors.ServerSelectionTimeoutError as e:
    print(f"Failed to connect to MongoDB: {e}")
    traceback.print_exc()
    client = None

# Database and Collections
if client:
    db = client["library"]
    books_collection = db["books"]
else:
    db = None
    books_collection = None

@app.route('/search', methods=['GET'])
def search_books():
    if books_collection is None:
        return jsonify({"message": "Database connection failed"}), 500

    try:
        query_params = request.args
        print(f"Query parameters received: {query_params}")

        search_criteria = {}

        if query_params.get("title"):
            search_criteria["title"] = {"$regex": query_params.get("title"), "$options": "i"}
        if query_params.get("author"):
            search_criteria["author"] = {"$regex": query_params.get("author"), "$options": "i"}
        if query_params.get("category"):
            search_criteria["category"] = {"$regex": query_params.get("category"), "$options": "i"}
        print(f"Search criteria: {search_criteria}")

        books = list(books_collection.find(search_criteria, {"_id": 0}))
        print(f"Books found: {books}")


        if books:
            print(f"test:")
            return jsonify({"books": books}), 200
        else:
            return jsonify({"message": "No books found matching the criteria"}), 404
    except Exception as e:

        print(f"Error occurred: {e}")
        return jsonify({"message": "Internal Server Error", "error": str(e)}), 501


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)

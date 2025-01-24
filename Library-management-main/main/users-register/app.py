from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient, errors

app = Flask(__name__)
CORS(app)  # Enable CORS for all requests

# MongoDB connection setup
try:
    client = MongoClient("mongodb+srv://matank222:ElzWhd3CUam4K8iw@library.l5ntd.mongodb.net/?retryWrites=true&w=majority&appName=library")
    # Ping MongoDB to check the connection
    client.admin.command('ping')
    print("Connected to MongoDB successfully")
except errors.ServerSelectionTimeoutError as e:
    print(f"Failed to connect to MongoDB: {e}")
    client = None

# Database and collection
db = client["library"]
users_collection = db["users"]

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    if not data or "username" not in data:
        return jsonify({"error": "Invalid data. 'username' is required."}), 400

    # Check if the username already exists in the database
    existing_user = users_collection.find_one({"username": data["username"]})
    if existing_user:
        return jsonify({"message": "Username already exists."}), 203
    elif existing_user is None:
            # If the username does not exist, save the user in the database
        user_id = users_collection.insert_one({
            "username": data["username"]
        }).inserted_id

        return jsonify({
            "message": "User registered successfully",
            "user": {
                "id": str(user_id),
                "username": data["username"]
            }
        }), 201
    else:
        return jsonify({"error": "External Error"}), 402
        
            
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

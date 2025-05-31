from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
db = client["fingerprint_db"]
collection = db["fingerprints"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/fingerprint', methods=['POST'])
def save_fingerprint():
    data = request.json
    fingerprint_hash = data.get('canvasHash')
    if not fingerprint_hash:
        return jsonify({"error": "Missing fingerprint hash"}), 400

    existing = collection.find_one({"canvasHash": fingerprint_hash})
    if existing:
        return jsonify({"message": "Fingerprint already exists", "firstSeen": existing["timestamp"]}), 200

    data["timestamp"] = datetime.utcnow()
    collection.insert_one(data)
    return jsonify({"message": "Fingerprint saved successfully"}), 201

@app.route('/api/fingerprints', methods=['GET'])
def get_fingerprints():
    fingerprints = list(collection.find({}, {"_id": 0}))
    return jsonify(fingerprints), 200

if __name__ == '__main__':
    app.run(debug=True)

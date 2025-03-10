# app.py
from flask import Flask, jsonify
from google.cloud import compute_v1
import os

app = Flask(__name__)

PROJECT_ID = os.environ.get("PROJECT_ID", "massive-tensor-452009-d2") # Set in Cloud Build or environment
ZONE = os.environ.get("ZONE", "us-central1-a")  # Default zone, can be overridden
VM_NAME = os.environ.get("VM_NAME", "my-test-vm") # Default VM name

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
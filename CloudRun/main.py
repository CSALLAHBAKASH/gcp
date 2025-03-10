from flask import Flask, request  # Import request from Flask
from google.cloud import pubsub_v1
import base64
import os

app = Flask(__name__)

# Replace with your project ID and subscription name
PROJECT_ID = "massive-tensor-452009-d2"
SUBSCRIPTION_NAME = "mytopic1-push"  # Just the subscription name

# Initialize the subscriber client (not strictly needed for push)
# subscriber = pubsub_v1.SubscriberClient()  # Remove this
# subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_NAME) # Remove this

@app.route("/", methods=["POST"])
def receive_message():
    """Receives and processes a Pub/Sub message."""
    try:
        # Get the message from the request (CORRECT WAY)
        message = request.get_json(silent=True)  # request, not requests

        if message and 'message' in message and 'data' in message['message']:
            data = message['message']['data']
            decoded_data = base64.b64decode(data).decode('utf-8')
            print(f"Received message: {decoded_data}")

            # ... your processing logic here ...

            return "Message processed", 200  # Acknowledge (200 OK)

        else:
            print("Invalid message format received.")
            return "Invalid message format", 400

    except Exception as e:
        print(f"Error processing message: {e}")
        return "Error processing message", 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    
    
# curl -X POST -H "Content-Type: application/json" -d '{"message": {"data": "SGVsbG8gV29ybGQh"}}' http://localhost:8080
# Message processed

# gcloud pubsub topics publish mytopic1 --message="Hello there13"
# 2025-02-26 15:52:58.783 IST Received message: Hello there13

# gcloud run services list
# gcloud run services delete mytestpush --region asia-south1
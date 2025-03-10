from google.cloud import pubsub_v1

def publish_message(project_id, topic_name, message):
    """Publishes a message to the given Pub/Sub topic."""

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    # Data must be a bytestring
    data = message.encode("utf-8")  # Convert string to bytes

    # Add attributes (optional)
    attributes = {"key": "value"}

    # Publish the message
    future = publisher.publish(topic_path, data, **attributes)
    message_id = future.result()  # Get the message ID

    print(f"Published message ID: {message_id}")
    return message_id

# Example usage:
project_id = "massive-tensor-452009-d2"  # Replace with your project ID
topic_name = "mytopic1"  # Replace with your topic name

while True:
    message = input("Enter message (or Ctrl+C to quit): ")
    if message.lower() == 'exit':  # Allow user to type 'exit' to quit.
        break
    try:
      message_id = publish_message(project_id, topic_name, message)
    except Exception as e:
      print(f"Error publishing message: {e}")
      break # Exit the loop if there's an error.
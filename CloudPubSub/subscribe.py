from google.cloud import pubsub_v1

def pull_messages(project_id, subscription_name):
    """Pulls messages from the given Pub/Sub subscription."""

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_name)

    def callback(message):
        """Callback function to handle received messages."""
        print(f"Received message: {message.data.decode('utf-8')}")
        message.ack()  # Acknowledge the message (important!)

    future = subscriber.subscribe(subscription_path, callback)
    print(f"Listening for messages on {subscription_path}..\n")

    try:
        # Keep the subscriber running
        future.result()  # Blocks indefinitely unless an exception occurs
        print(future.result())  # Blocks indefinitely unless an exception occurs
    except KeyboardInterrupt:
        # future.cancel()  # Stop the subscriber gracefully
        pass

# Example usage:
project_id = "massive-tensor-452009-d2"
subscription_name = "mytopic1-sub"

pull_messages(project_id, subscription_name)
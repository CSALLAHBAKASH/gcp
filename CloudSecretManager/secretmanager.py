# Import the Secret Manager client library.
from google.cloud import secretmanager

project_id = "massive-tensor-452009-d2"
secret_id = "test-1"

client = secretmanager.SecretManagerServiceClient()

parent = f"projects/{project_id}"

secret = client.create_secret(
    request={
        "parent": parent,
        "secret_id": secret_id,
        "secret": {"replication": {"automatic": {}}},
    }
)

# Add the secret version.
version = client.add_secret_version(
    request={"parent": secret.name, "payload": {"data": b"hello world!"}}
)

# Access the secret version.
response = client.access_secret_version(request={"name": version.name})

payload = response.payload.data.decode("UTF-8")
print(f"Plaintext: {payload}")
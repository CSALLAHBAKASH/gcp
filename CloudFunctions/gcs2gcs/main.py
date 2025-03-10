import functions_framework

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def hello_gcs(cloud_event):
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    bucket = data["bucket"]
    name = data["name"]
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]

    print(f"Event ID: {event_id}")
    print(f"Event type: {event_type}")
    print(f"Bucket: {bucket}")
    print(f"File: {name}")
    print(f"Metageneration: {metageneration}")
    print(f"Created: {timeCreated}")
    print(f"Updated: {updated}")

    print()
    print(cloud_event)
    
    if name == "citycd.csv":
        from google.cloud import storage

        client = storage.Client()
        bucket1 = client.bucket("mominali_gcs_10")
        blob1 = bucket1.blob("citycd.csv")

        bucket2 = client.bucket("mominali_gcs_2")
        bucket2.copy_blob(blob1,bucket2, "citycd.csv")
        
        print("Copied to destination")
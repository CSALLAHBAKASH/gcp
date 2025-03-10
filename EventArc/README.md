gcloud eventarc providers list

gcloud eventarc providers describe \
  pubsub.googleapis.com


# Create a Cloud Run sink

export SERVICE_NAME=event-display
export IMAGE_NAME="gcr.io/cloudrun/hello"
gcloud run deploy ${SERVICE_NAME} \
  --image ${IMAGE_NAME} \
  --allow-unauthenticated \
  --max-instances=3

gcloud run services list
gcloud run services delete hello --region us-central1


# Create a Cloud Pub/Sub event trigger

gcloud eventarc providers describe \
  pubsub.googleapis.com

gcloud eventarc triggers create trigger-pubsub \
  --destination-run-service=${SERVICE_NAME} \
  --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished"

export TOPIC_ID=$(gcloud eventarc triggers describe trigger-pubsub \
  --format='value(transport.pubsub.topic)')

echo ${TOPIC_ID}


# Test the trigger
gcloud eventarc triggers list

gcloud pubsub topics publish ${TOPIC_ID} --message="Hello there"

gcloud eventarc triggers delete trigger-pubsub


----------------------------------------------------------------------------------------------

# Create a Audit Logs event trigger

export BUCKET_NAME=$(gcloud config get-value project)-cr-bucket

gsutil mb -p $(gcloud config get-value project) \
  -l $(gcloud config get-value run/region) \
  gs://${BUCKET_NAME}/

echo "Hello World" > random.txt
gsutil cp random.txt gs://${BUCKET_NAME}/random.txt


## Create a trigger

gcloud eventarc providers describe cloudaudit.googleapis.com

gcloud eventarc triggers create trigger-auditlog \
  --destination-run-service=${SERVICE_NAME} \
  --event-filters="type=google.cloud.audit.log.v1.written" \
  --event-filters="serviceName=storage.googleapis.com" \
  --event-filters="methodName=storage.objects.create" \
  --service-account=${PROJECT_NUMBER}-compute@developer.gserviceaccount.com

## Test the trigger

gcloud eventarc triggers list
gsutil cp random.txt gs://${BUCKET_NAME}/random.txt

## Delete trigger
gcloud eventarc triggers delete trigger-auditlog
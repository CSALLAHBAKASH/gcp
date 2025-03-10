gcloud auth configure-docker us-central1-docker.pkg.dev


gcloud builds submit --region=REGION --tag gcr.io/PROJECT_ID/IMAGE_NAME .
gcloud builds submit --region=REGION --config=BUILD_CONFIG_FILE .
gcloud builds list
gcloud builds describe BUILD_ID


# Example Cloud Build step to push an image
gcloud builds submit --region=us-west2 --tag gcr.io/my-project/my-image .

# Then, use Cloud Deploy to create a delivery pipeline via the Cloud Console or API.

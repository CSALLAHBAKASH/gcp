
export PROJECT_ID=$(gcloud config get-value project)

gcloud artifacts repositories create example-docker-repo --repository-format=docker \
    --location=us-central1 --description="Docker repository" \
    --project=$PROJECT_ID

gcloud artifacts repositories list \
    --project=$PROJECT_ID


gcloud auth configure-docker us-central1-docker.pkg.dev


docker pull us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0



docker tag us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0 \
us-central1-docker.pkg.dev/$PROJECT_ID/example-docker-repo/sample-image:tag1


docker push us-central1-docker.pkg.dev/$PROJECT_ID/example-docker-repo/sample-image:tag1


docker pull us-central1-docker.pkg.dev/$PROJECT_ID/example-docker-repo/sample-image:tag1

















gcloud services enable artifactregistry.googleapis.com


gcloud artifacts repositories create REPOSITORY_ID \
    --repository-format=FORMAT \
    --location=LOCATION \
    --description=DESCRIPTION


gcloud artifacts repositories create my-repo \
    --repository-format=docker \
    --location=us-central1 \
    --description="My Docker Repository"


gcloud artifacts repositories list


gcloud artifacts repositories list-packages REPOSITORY_ID


gcloud artifacts packages list-versions PACKAGE_ID --repository=REPOSITORY_ID


gcloud auth configure-docker LOCATION-docker.pkg.dev


docker tag LOCAL_IMAGE LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_ID/IMAGE_NAME
docker push LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_ID/IMAGE_NAME


docker pull LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_ID/IMAGE_NAME


gcloud artifacts repositories describe REPOSITORY_ID


gcloud artifacts repositories delete REPOSITORY_ID

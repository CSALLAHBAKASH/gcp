# Log in to GCP
gcloud auth login

# Configure Docker to use GCP credentials
gcloud auth configure-docker

# Set default project
gcloud config set project <PROJECT_ID>





# List all repositories in project
gcloud container images list

# List images in a specific repository
gcloud container images list --repository=gcr.io/<PROJECT_ID>/<REPO_NAME>

# List tags for a specific image
gcloud container images list-tags gcr.io/<PROJECT_ID>/<IMAGE_NAME>




# Tag a local Docker image
docker tag <LOCAL_IMAGE> gcr.io/<PROJECT_ID>/<IMAGE_NAME>:<TAG>

# Push to GCR
docker push gcr.io/<PROJECT_ID>/<IMAGE_NAME>:<TAG>

# Pull from GCR
docker pull gcr.io/<PROJECT_ID>/<IMAGE_NAME>:<TAG>




# Delete specific image tag
gcloud container images delete gcr.io/<PROJECT_ID>/<IMAGE_NAME>:<TAG>

# Delete all untagged images
gcloud container images delete gcr.io/<PROJECT_ID>/<IMAGE_NAME> --force-delete-tags




# Scan images for vulnerabilities
cnspec scan container registry gcr.io/<PROJECT_ID>/<REPO_NAME>

# Search across all repositories
gcloud artifacts docker images list




gcloud artifacts repositories list
gcloud artifacts docker tags list <LOCATION>-docker.pkg.dev/<PROJECT>/<REPO>/<IMAGE>

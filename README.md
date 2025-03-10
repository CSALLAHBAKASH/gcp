
PROJECT_ID=massive-tensor-452009-d2



```python
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_.json_credential_file"
```

```bash
export GOOGLE_APPLICATION_CREDENTIALS='./massive-tensor-452009-d2-eb92f07f6b7d.json'
```

```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
```

restart terminial

```bash
gcloud init
gcloud config list
gcloud config get compute/regin
```

```bash
pip install google-cloud-storage

```

```bash
# DefaultCredentialsError: Your default credentials were not found.
gcloud auth application-default login
```

```bash

gcloud services enable \
    compute.googleapis.com \
    run.googleapis.com \
    cloudbuild.googleapis.com \
    artifactregistry.googleapis.com \
    cloudbuild.googleapis.com \
    run.googleapis.com \
    cloudfunctions.googleapis.com \
    eventarc.googleapis.com \
    logging.googleapis.com \
    pubsub.googleapis.com

```



gh repo create --source=. --public
git remote add origin https://github.com/CSALLAHBAKASH/gcp.git
git push -u origin master or git push --set-upstream origin master







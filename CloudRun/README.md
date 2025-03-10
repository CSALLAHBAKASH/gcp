### Test locally then deploy
```
gcloud run deploy --source .


gcloud run deploy mytestpush --source . --region asia-south1 --platform managed --allow-unauthenticated 
```

API enable - artifactregistry, cloudbuild, run

region - required

# example
```
gcloud run deploy my-backend --image=us-docker.pkg.dev/project/image
```

To deploy to Cloud Run on Kubernetes Engine, you need to specify a cluster:
```
gcloud run deploy --image=us-docker.pkg.dev/project/image --cluster=my-cluster
```

```bash
gcloud run services list
gcloud run services describe mominali
gcloud run services describe mominali --region asia-south1 --format yaml
gcloud run services describe mominali --region asia-south1 --format export
gcloud run services describe mominali --region asia-south1 --format='value(status.url)'
gcloud beta run services update mominali --scaling=0
gcloud run services delete mominali --region asia-south1
```
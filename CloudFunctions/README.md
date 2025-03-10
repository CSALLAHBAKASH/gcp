
```bash 
gcloud functions deploy copy_file_on_event \
  --runtime python39 \
  --trigger-event google.cloud.storage.object.v1.finalized \
  --trigger-resource mominali_gcs_1 \  
  --source . \
  --region us-central1
```

bucket and trigger/function should be same location/region
cat << EOF > request.json
{
    "endpoint": "projects/massive-tensor-452009-d2/locations/us-central1/publishers/google/models/imagen-3.0-generate-002",
    "instances": [
        {
            "prompt": "lion with tiger running and chasing  deer",
        }
    ],
    "parameters": {
        "aspectRatio": "16:9",
        "sampleCount": 4,
        "negativePrompt": "",
        "enhancePrompt": false,
        "personGeneration": "",
        "safetySetting": "",
        "addWatermark": true,
        "includeRaiReason": true,
        "language": "auto",
    }
}
EOF

#%% bash

PROJECT_ID="massive-tensor-452009-d2"
LOCATION_ID="us-central1"
API_ENDPOINT="us-central1-aiplatform.googleapis.com"
MODEL_ID="imagen-3.0-generate-002"

curl \
-X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://${API_ENDPOINT}/v1/projects/${PROJECT_ID}/locations/${LOCATION_ID}/publishers/google/models/${MODEL_ID}:predict" -d '@request.json'
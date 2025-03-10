from google.cloud import translate_v3 as translate

DATASET_ID = "example-set3"
PROJECT_ID = "massive-tensor-452009-d2"
LOCATION = "us-central1"
GCS_URI = "gs://mominali_gcs_1/file.tsv"  # Replace with your GCS URI

def create_adaptive_mt_dataset():
    client = translate.TranslationServiceClient()
    adaptive_mt_dataset = translate.types.AdaptiveMtDataset()
    adaptive_mt_dataset.name = f"projects/{PROJECT_ID}/locations/{LOCATION}/adaptiveMtDatasets/{DATASET_ID}"
    adaptive_mt_dataset.display_name = "Example set"
    adaptive_mt_dataset.source_language_code = "en"
    adaptive_mt_dataset.target_language_code = "ar"
    request = translate.CreateAdaptiveMtDatasetRequest(
        parent=f"projects/{PROJECT_ID}/locations/{LOCATION}",
        adaptive_mt_dataset=adaptive_mt_dataset,
    )
    response = client.create_adaptive_mt_dataset(request=request)
    print(response)

def import_adaptive_mt_file():
    client = translate.TranslationServiceClient()
    input_config = translate.types.ImportAdaptiveMtFileRequest.GcsInputConfig(gcs_uri=GCS_URI)
    request = translate.ImportAdaptiveMtFileRequest(
        parent=f"projects/{PROJECT_ID}/locations/{LOCATION}/adaptiveMtDatasets/{DATASET_ID}",
        gcs_input_config=input_config,
    )
    response = client.import_adaptive_mt_file(request=request)
    print(response)

def adaptive_mt_translate():
    client = translate.TranslationServiceClient()
    request = translate.AdaptiveMtTranslateRequest(
        parent=f"projects/{PROJECT_ID}/locations/{LOCATION}",
        dataset=f"projects/{PROJECT_ID}/locations/{LOCATION}/adaptiveMtDatasets/{DATASET_ID}",
        content=["hello, how are you doing. how many times prophet mosa in quraan"],
    )
    response = client.adaptive_mt_translate(request=request)
    print(response)

# 1. Create the dataset
create_adaptive_mt_dataset()

# 2. Import the file (after uploading to GCS and replacing YOUR_BUCKET_NAME and YOUR_FILE.tsv)
import_adaptive_mt_file()

# 3. Translate using the adaptive model
adaptive_mt_translate()
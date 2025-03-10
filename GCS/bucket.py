


#%%
from google.cloud import storage

client = storage.Client()
buckets = client.list_buckets()
for i in buckets:
    print(i.name)



#%%

## create bucket
# gsutil mb -p <project-id> -l <region> gs://mominali_gcs_1

from google.cloud import storage
client = storage.Client()
bucket = client.create_bucket("mominali_gcs_2")
print("bucket created")


# %%

## list blobs >> folders/files
from google.cloud import storage
client = storage.Client()
blobs = client.list_blobs("mominali_gcs_1")
for blob in blobs:
    print(blob.name)


# %%

## activating bucket and blob
bucket = client.bucket("mominali_gcs_1")
print(bucket.name)
blob = bucket.blob("fold1/Advertising.csv")
print(blob.name)

## delete blob >> folder/file
blob.delete()



# %%

## list blobs and if folder/file delete
bucket = client.bucket("mominali_gcs_1")
blobs = bucket.list_blobs()
for blob in blobs:
    if "fold1" in blob.name:
        print(blob.name)
        print(blob.delete())



# %%

## upload from local
bucket = client.bucket("mominali_gcs_1")
blob = bucket.blob("fold1/test.txt")
blob.upload_from_filename("test.txt")


# %%
## copy file
bucket1 = client.bucket("mominali_gcs_1")
blob1 = bucket.blob("fold1/test.txt")

bucket2 = client.bucket("mominali_gcs_2")
bucket2.copy_blob(blob1,bucket2, "test.txt")


# %%

## move file or copy and delete source
bucket1 = client.bucket("mominali_gcs_1")
blob1 = bucket.blob("fold2/citycd.csv")

bucket2 = client.bucket("mominali_gcs_2")
bucket2.copy_blob(blob1,bucket2, "citycd.csv")
blob1.delete()

# %%
from google.cloud import storage

client = storage.Client()
bucket1 = client.bucket("mominali_gcs_10")
blob1 = bucket1.blob("citycd.csv")

bucket2 = client.bucket("mominali_gcs_2")
bucket2.copy_blob(blob1,bucket2, "citycd.csv")

print("Copied to destination")
# %%

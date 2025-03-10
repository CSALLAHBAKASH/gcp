#%%
from google.cloud import bigquery
from google.cloud import storage
import os

#%%
# Define constants
PROJECT_ID = os.environ.get('PROJECT_ID')
DATASET_ID = os.environ.get('DATASET_ID')
TABLE_ID = os.environ.get('TABLE_ID')
BUCKET_NAME = os.environ.get('BUCKET_NAME')

def load_data_to_bigquery(event, context):
    # Create clients
    client = bigquery.Client()
    storage_client = storage.Client()

    # Get the uploaded file from GCS
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(event['name'])
    
    # Define the BigQuery table
    table_id = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
    
    # Configure the load job
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,  # Optional: Skip header row
        autodetect=True  # Optional: Auto-detect schema
    )
    
    # Load data from GCS to BigQuery
    load_job = client.load_table_from_uri(
        f"gs://{BUCKET_NAME}/{event['name']}",
        table_id,
        job_config=job_config
    )
    
    # Wait for the load job to complete
    load_job.result()
    
    print(f"Loaded {event['name']} into {table_id}")


#%%

from google.cloud import bigquery

client = bigquery.Client()
query = """
  SELECT name, COUNT(*) as total
  FROM `bigquery-public-data.usa_names.usa_1910_2013`
  WHERE state = 'TX'
  GROUP BY name
  LIMIT 20
"""

results = client.query_and_wait(query)  # Returns row iterator
for row in results:
    print(row.name, row.total)



#%%



#%%


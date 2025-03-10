import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

# Define pipeline options
options = PipelineOptions(
    flags=None,
    runner='DataflowRunner',
    project='massive-tensor-452009-d2',
    temp_location='gs://mominali_gcs_10/temp/',
    staging_location='gs://mominali_gcs_10/stage/',
    region='us-central1'
)

with beam.Pipeline(options=options) as p:
    
    p | "gcs2gcs" >> beam.io.ReadFromText("gs://mominali_gcs_10/citycd.csv") | beam.io.WriteToText("gs://mominali_gcs_2/citycd.csv")
    
    
    
# python gcs2gcs.py 
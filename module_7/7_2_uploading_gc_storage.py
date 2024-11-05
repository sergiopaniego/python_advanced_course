from google.cloud import storage

# Initialize a storage client
client = storage.Client()

# Specify the bucket name
bucket_name = 'gcp_course_example_bucket'
bucket = client.bucket(bucket_name)

# Specify the file to upload and the blob name
source_file_name = 'example.txt'  # Local file path
destination_blob_name = 'file.txt'  # Blob name in the bucket

# Upload the file
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(source_file_name)

print(f'File {source_file_name} uploaded to {destination_blob_name}.')

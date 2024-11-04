from google.cloud import storage

# Initialize a storage client
client = storage.Client()

# Specify the bucket name
bucket_name = 'your-bucket-name'
bucket = client.bucket(bucket_name)

# Specify the file to download
source_blob_name = 'file.txt'  # Blob name in the bucket
destination_file_name = 'path/to/downloaded/file.txt'  # Local path to save the file

# Download the file
blob = bucket.blob(source_blob_name)
blob.download_to_filename(destination_file_name)

print(f'Blob {source_blob_name} downloaded to {destination_file_name}.')

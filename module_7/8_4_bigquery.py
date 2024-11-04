
from google.cloud import bigquery

# Initialize BigQuery client
client = bigquery.Client()

# Define a query
query = """
    SELECT name, age FROM `your-project-id.your_dataset.users`
    WHERE age > 25
"""

# Run the query
query_job = client.query(query)

# Print the results
for row in query_job:
    print(f'Name: {row.name}, Age: {row.age}')

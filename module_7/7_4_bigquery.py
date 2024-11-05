
from google.cloud import bigquery

# Initialize BigQuery client
client = bigquery.Client()

# Define a query
#query = """
#    SELECT name, age FROM `your-project-id.your_dataset.users`
#    WHERE age > 25
#"""

query = """
    SELECT name, COUNT(*) as total
    FROM `bigquery-public-data.usa_names.usa_1910_current`
    WHERE state = 'TX'
    GROUP BY name
    ORDER BY total DESC
    LIMIT 10
"""

query_job = client.query(query)  # Execute query

# Obtain results
results = query_job.result()  # Wait for the query to be completed

# Show the results
for row in results:
    print(f'Name: {row.name}, Total: {row.total}')


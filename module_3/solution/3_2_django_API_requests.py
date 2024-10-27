import requests

# URL of the API endpoint
url = 'http://127.0.0.1:8000/api/books/'

# Data to be sent in the POST request
data = {
    "title": "New Book",
    "author": "Author Name",
    "published_date": "2023-10-01",
    "summary": "A brief summary of the new book."
}

# Making the POST request
response = requests.post(url, json=data)

# Checking the response
if response.status_code == 201:
    print("Book created successfully!")
    print("Response data:", response.json())
else:
    print("Failed to create book.")
    print("Status code:", response.status_code)
    print("Response data:", response.json())
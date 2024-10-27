import requests

# Define the base URL for the Cat Facts API
base_url = "https://catfact.ninja"

# Task 1: Make a GET request to retrieve a random cat fact
response = requests.get(f"{base_url}/fact")
print("GET Request to retrieve a random cat fact")
print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print("Random Cat Fact:", data["fact"])  # Display the cat fact
else:
    print("Failed to retrieve data.")

print("\n" + "-"*40)

# Task 2: Make a GET request to retrieve a list of cat facts (limit to 3 facts)
response = requests.get(f"{base_url}/facts", params={"limit": 3})
print("GET Request to retrieve a list of cat facts (limit 3)")
print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    for index, fact in enumerate(data["data"], start=1):
        print(f"Fact {index}: {fact['fact']}")
else:
    print("Failed to retrieve data.")

print("\n" + "-"*40)

# Task 3: Intentionally cause an error by making a GET request to a non-existent endpoint
response = requests.get(f"{base_url}/nonexistent")
print("GET Request to a non-existent endpoint (should return 404)")
print("Status Code:", response.status_code)

if response.status_code == 404:
    print("Endpoint not found.")

print("\n" + "-"*40)

# Task 4: Handle the response text and JSON parsing
response = requests.get(f"{base_url}/fact")
print("GET Request with response handling")
print("Status Code:", response.status_code)

try:
    data = response.json()
    print("JSON Parsed Response:", data)
except ValueError:
    print("Failed to parse JSON response.")
print("Raw Text Response:", response.text)
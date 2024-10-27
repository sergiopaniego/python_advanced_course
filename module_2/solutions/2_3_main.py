from api_module import fetch_data

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    data = fetch_data(url)

    if data:
        print(f"Fetched {len(data)} posts.")
        # Optional: Print the first post to show the data structure
        print(data[0])  
    else:
        print("Failed to fetch data.")

import requests

def fetch_data(url):
    """
    Fetch data from the given URL and return it as a JSON object.
    
    :param url: URL to fetch data from
    :return: JSON data or None if the request failed
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

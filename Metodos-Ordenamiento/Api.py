import requests

def fetch_data():
    url = "https://www.datos.gov.co/resource/uea5-is6n.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch data from API")
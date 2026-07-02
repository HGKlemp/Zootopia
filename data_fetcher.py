import requests


API_KEY = "qGpr3WKnTJfpUO6FLSUcQ1kRZFdoTMsAfMhABqIz"  # 10x X = dein API Key hier einsetzen

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
            ...
        },
        'locations': [
            ...
        ],
        'characteristics': {
            ...
        }
    },
    """

    url = "https://api.api-ninjas.com/v1/animals"

    headers = {
        "X-Api-Key": API_KEY
    }

    params = {
        "name": animal_name
    }

    response = requests.get(url, headers=headers, params=params)

    # Successful request
    if response.status_code == 200:
        data = response.json()
        return data

    return []
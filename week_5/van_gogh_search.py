import requests
import json

url = 'https://collectionapi.metmuseum.org/public/collection/v1/search'

params = {
    'q' : 'van gogh',
    'isOnView' : 'true',
    'hasImages' : 'true'
}

r = requests.get(url, params=params)
data = json.loads(r.text)
print(json.dumps(data, indent=2))
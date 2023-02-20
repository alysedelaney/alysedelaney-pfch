import requests
import json

van_gogh_object_ids = []

url = 'https://collectionapi.metmuseum.org/public/collection/v1/search'

params = {
    'q' : 'van gogh',
    'isOnView' : 'TRUE',
    'hasImages' : 'TRUE'
}

r = requests.get(url, params=params)
data = json.loads(r.text)

van_gogh_object_ids = data['objectIDs']

artwork_info = []

for artwork in van_gogh_object_ids: 
    artwork_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{artwork}"
    artwork_r = requests.get(artwork_url)
    artwork_data = json.loads(artwork_r.text)
    artwork_info.append(artwork_data)

artwork_titles = []

for entry in artwork_info: 
    artwork_titles.append(entry['title'])

print(artwork_titles)


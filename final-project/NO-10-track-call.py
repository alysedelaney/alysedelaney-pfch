import requests 
import base64
import json

# Spotify API Set Up ------------------------------------------------------

client_id = "5bae1e05720d486a8bef2310f63cdb05"
client_secret = "8a701744762d47ae801d7bebf730e489"

url = 'https://accounts.spotify.com/api/token'

headers = {}
data = {}

message = f"{client_id}:{client_secret}" 
message_bytes = message.encode('ascii')
base64bytes = base64.b64encode(message_bytes)
base64message = base64bytes.decode('ascii')

headers['Authorization'] = f"Basic {base64message}"
data['grant_type'] = "client_credentials"

r = requests.post(url, headers=headers, data=data)

token = r.json()['access_token']

headers = {
    "Authorization": "Bearer " + token
}

base_url = "https://api.spotify.com/v1/"

#-------------------------------------------------

track_ids = []
search_lists = []

with open('artist-track-ids.json') as read_file:
    artist_ids_json = json.load(read_file)

    for entry in artist_ids_json:
        for track in entry['tracks']:
            track_ids.append(track)
    
    # print(track_ids)

    def split(list_a, chunk_size):

        for i in range(0, len(list_a), chunk_size):
            yield list_a[i:i + chunk_size]

    chunk_size = 50
    track_ids_split = list(split(track_ids, chunk_size))
    
    for section in track_ids_split:
        section_joined = ",".join(section)
        search_lists.append(section_joined)
    
tracks_url = f"{base_url}tracks"
features_url = f"{base_url}audio-features"

track_features = []
track_data = []

batch_counter = 1

for search in search_lists:
    print(f"{batch_counter}/{len(search_lists)}")
    params = {
        "ids" : search
    }

    tracks_res = requests.get(url=tracks_url, headers=headers, params=params)
    tracks_json = tracks_res.json()
    track_data.append(tracks_json['tracks'])
    json.dump(track_data, open('remaining-track-data.json', 'w'), indent=2)
    
    features_res = requests.get(url=features_url, headers=headers, params=params)
    features_json = features_res.json()
    track_features.append(features_json['audio_features'])
    json.dump(track_features, open('remaining-track-features.json', 'w'), indent=2)

    batch_counter += 1




# my_list = ['6UnCGAEmrbGIOSmGRZQ1M2', '3Y8XpUFQzTGSEDuApfyJV1', '6PyZGb1rB7oLKCICWTmGYa', '2kvwSbG26eHKUJdvH7DiR2']

# joined = ",".join(my_list)

# print(joined)
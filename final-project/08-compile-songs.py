import requests 
import base64
import json
import os
import time

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

#-----------------------------------------------------------------

compiled_artist_info = []

path_json = 'data/song_data_by_artist/'
#get all JSON file names as a list
json_files = [filename for filename in os.listdir(path_json) if filename.endswith('.json')]

num_files = len(json_files)

compiled_song_info = []

for json_file_name in json_files:
    with open(os.path.join(path_json, json_file_name)) as json_file:
        json_load = json.load(json_file)

        artist_name = json_load['artist_name']
        artist_spotify_id = json_load['spotify_id']
        
        song_info = []

        for song in json_load['songs']:

            song_spotify_id = song['spotify_id']
            genius_id = song['search_results']['id']
            lyrics_state = song['search_results']['lyrics_state']
            lyrics = song['search_results']['lyrics']
            language = song['search_results']['language']
            song_stat_hot = song['search_results']['stats']['hot']
            song_title = song['search_results']['title']
            description = song['full_song_data']['song']['description']['plain']
            release_date = song['full_song_data']['song']['release_date']
            primary_artist = song['full_song_data']['song']['primary_artist']['name']

            writers = []
            for writer in song['full_song_data']['song']['writer_artists']:
                writer_name = writer['name']
                writers.append(writer_name)
            
            producers = []
            for producer in song['full_song_data']['song']['producer_artists']:
                producer_name = producer['name']
                producers.append(producer_name)
            
            annotations = song['annotations']

            song_data = {
                "title" : song_title,
                "primary_artist" : primary_artist,
                "spotify_id" : song_spotify_id,
                "genius_id" : genius_id,
                "description" : description,
                "writers" : writers,
                "producers" : producers,
                "release_date" : release_date,
                "lyrics" : lyrics,
                "hot" : song_stat_hot,
                "annotations" : annotations
            }

            if lyrics_state == "complete" and language == "en":
                song_info.append(song_data)
        
        artist_info = {
            "artist_name" : artist_name,
            "spotify_id" : artist_spotify_id,
            "songs" : song_info
        }

        compiled_song_info.append(artist_info)


with open('data/compiled_song_info.json', 'w') as write_file:
    json.dump(compiled_song_info, write_file, indent=2)
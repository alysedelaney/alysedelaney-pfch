import requests 
import base64
import json
import time

# API Set Up ------------------------------------------------------

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

#-------------------------------------------------------------

searches = ["Lucy Dacus", "Phoebe Bridgers", "Julien Baker", "Mitski", "Snail Mail", "Soccer Mommy", "Waxahatchee", "Japanese Breakfast", "Adrienne Lenker", "Julia Jacklin", "Angel Olsen", "Sharon van Etten", "Jay Som", "Clairo", "mxmtoon", "girl in red", "beabadoobee", "Samia", "Wallice", "Blu Eyes", "Jordana", "Orla Gartland", "Renee Rapp", "Grace Ives", "Indigo De Zouza", "Remi Wolf", "Willow", "Kate Bollinger", "Becca Mancari", "Wilma Laverne Miner", "Margaret Glaspy", "Jade Bird", "Ada Lea", "Delaney Bailey", "Angie McMahon", "Natalie Prass", "Arlo Parks", "Dora Jar", "Frankie Cosmos", "Cornelia Murr", "Maggie Rogers"]

artist_ids = []
related_unique_ids = []
related_unqiue_names = []
artist_list = []

print(f"\nRetrieving IDs for {len(searches)} artists...")

#search artist names for their spotify ids

counter = 1 
for search in searches:
    search_url = f"https://api.spotify.com/v1/search/"
    search_params = {
        "q" : search,
        "type" : "artist",
        "limit" : 1
    }

    search_res = requests.get(url=search_url, headers=headers, params=search_params)
    search_json = search_res.json() 
    artist_id = search_json['artists']['items'][0]['id']
    artist_name = search_json['artists']['items'][0]['name']
    artist_info = {
        "name" : artist_name,
        "id" : artist_id
    }
    print(f"{counter}: {artist_name}")
    artist_ids.append(artist_id)
    related_unique_ids.append(artist_id)
    artist_list.append(artist_info)
    time.sleep(.5)
    counter += 1

#use ids to compile master list of related artists
print(f"\nFinding related artists...")

for artist_id in artist_ids:
    print(f"{artist_id}----------")
    related_url = f"https://api.spotify.com/v1/artists/{artist_id}/related-artists"
    related_res = requests.get(url=related_url, headers=headers)
    related_json = related_res.json()

    for result in related_json['artists']:

        if result['id'] not in related_unique_ids:
            related_unique_ids.append(result['id'])
            related_unqiue_names.append(result['name'])
            print(result['name'])
            artist_info = {
                "name" : result['name'],
                "id" : result['id'],
            }
            artist_list.append(artist_info)
            time.sleep(.5)

print(f"{len(artist_list)} related artists found:")

print(f"\n{related_unqiue_names}\n")

with open(f"data/all-related-artists.json", 'w') as write_file:
    json.dump(artist_list, write_file, indent=2)

print("File written.")
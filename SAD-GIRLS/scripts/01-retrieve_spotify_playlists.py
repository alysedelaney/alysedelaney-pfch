import requests 
import base64
import json

# =========================================================================

# The first of my attempts to create a list of artists to analyze. This script collects the contents of ~200 playlists on Spotify labeled as "bedroom pop" and outputs it to a json file. 

# =========================================================================

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

# ----------------------------------------------------------------

search_ids = ["37i9dQZF1DXcxvFzl58uP7","3gaoyDYexk55UAzx6Am9XK","4yks3K209VitZB8oAMg8lq","5vyn8RpVqDNvy9I5jiE6id","0n289Qud0v93aLPNdMp9B1","58VSrAoap9gvA8KTvuNisn","5cvQYoTyU3OFkBHzWHlfwA","5HDfqJz4Sw7JSTa8ITRhOQ","6nPnA0w9JNtfIkiBZgLfUm","0wySos1GKtnnh8LPVC1CaK","6DtQQKzpH0jAMCuWahgpDE","5ttX57I8BVrpPGfvm22wFP","0FVy2PfjwugL7FRYghh7Ip","339zjWDksACL7sNs2UehlX","5GsdS5wAlGuRNikVL8gNuA","3Ya1gLSdj0ho31U43zwTBZ","6Pmv9Nroqy3AvtW71ZwK4d","1lRLjY4mYIWOsGapVv9lVP","3z6xt4PeWgsKbCcuhex13J","3CSChNl2ErECOQ78YtpJDY","7co6L0q3OekFPbdzaefGyX","2pegkuG8RfFwAaazFehhIB","1INhLhysXB9it2ygC3wMBy","4J90Ilt1FH0NXKwT8nUYeV","3nwN5QpXQieWYC8KbRZ3QJ","6trdfCG2yW5kwGOpJpD2JD","1BTipVF6sgJ81ealWpWRtW","1Oep5FCsGRLN3XyLkYrGDp","5uw97HaPSaBZhBJ4waxn59","06FfQFdOFs650SyRCXvOiL","3uYyfsENJLepkkiPHu9KjN","2CGlthFIsTQUgSfmTGODCu","3kgbgymuMCbSRk0F67MhgK","1qUWcvht8DLprHNr9BXcoo","5XFXHv5J7XjgJ1hJ6fIgJQ","02IjtnW4NioQjWRqn3CN1s","2fJFFhvaHoXRQIJybNzPvV","4rnOw5M2YAekvMn2EygvpD","7ednG9nieArj8hUqGp4sLJ","0XcpICvViVuZZsBvMsiZ0C","4mZsRXv6n8LqQrerUuvYaT","7D3kJ6ciUnNQDnNbUyU5Xb","2mh8yBBzbX36VBfL8uKk6z","4lQ3DI6jY92jGg7zqRbjo4","47NRZmdWKzLVHfP8mYUUfl","6YeOTcLLYrdJm7kvynmQwM","4ucJexAGHInGFFX4FP1Zlo","5xdq1qtjjwrDHsBzaAYyXt","0wutezn60J0xpNoU8c0drw","40rokIYuOOP2p1WFukeAns","6pYhR6rzNYx01E1fLF5lo2","1w2jy15RMOU40kpIAzDzfa","4m361xfDNlwccUS2xN13HH","01m7zM0RrUwsQ20YKKcwyu","5QyETYTN1WQK3ETevOde0b","7sClDbpxLRlE0Ei1U9eWHZ","2OO9JBit0gRvQmD0BYX2LD","1XgUp80vKfyngOtskdiPGt","6hV50MLbSCd8wSEL07phZY","2Yht4Vkp7QEnU53PAYrLMl","7qijZrgSpGBrmiBlrWSN78","19FmzzqWIL0weu5DQGoLwF","0bD6AstUOrrx2o2Pb0lQGA","4D4JF5IAEUlIef6wZj0KZa","2gpEIY06uaYOQiLFGF6HuF","1wn3zQteb6I2ILBPUvV596","5hoMJGcth9Dx8dc5ihq1pv","1pBtOgLzwAlhruEpTe9e52","5AGsm6Q27VAL66gfZu0UpH","3Cn6YQVrlyzx2yYlpxvZGO","73KalXHX0iBfiEdQviBgNh","5OBfZdPGEosdipeCym8dXj","7K659Ne2Wh6J7F1YI458kN","2IZQVBk6m9pFXVA3SEDJDS","3My3agYpVrvW2HxEJMUsjm","2a9C5swZ1GlsHO9y0OhhwF","0URTxZxeBQ6JElVvL9GqOe","3b1wgMJeVarNxmgcQFPnbN","1QTYUiQe6uz6z5G4TtqiAr","73NkmXRuZ0qw5Dub7KGXgq","4nT9D8R03CWt2A7nyQEMqA","5QUPBPd0RUj4DjuroedbUK","0IKpm1wMeDBVLY4oYMo91w","5xtkHqEUuRK3FpWrkclloC","6rtwM7Lk7TXcldUaYPxxe3","2fPWX5OK40DISH9HAdCZ4o","7aVK60vht5FrGFQfKBJaEO","7Cxyx3WzywjZf8XTEPGX9O","1zeXvPC1G7XRjPKeLWWVJA","2vfFYCUaa52TvHmvpgRZtA","2mHoxd7L3ShAE61Gc8Unmo","0urQ3YrJOMHa0G1YPYwG57","3XgCiABIdEBBP0Ru6FF6em","2Qzt7afSQZh4QXm2RRMI8w","0QNyYTyL4R4QI4eBl2DfzL","5kKlPcNF34EIMJl5phaT67","41vohFwrq05YeNGYfKyZxy","2MquF4QqGrtpaxZN2ZPMjc","4d0RNDhJrE6XJtXVjjVEyd","3hAtWn6auNhaoit8rrhg4Q","7bTFg6dLyFjXj27MJBTys4","7blx2OJhzftatVcnoMIh05","0j9unkHMljM3z3fQH4FcFe","4yv27FmfhGwblTzjpsxYry","2cHW0CPCGcUP0orVDwdyIm","6PYkRaTcB4bboTfizpkyZ1","14pLtHPiUhYHdNBtyLJsjV","5rr0fuf3YzIJ6qXeCQZnp5","4uvzbdA4wCY62we7r8v099","40W7cWPB0k0ZKv0JageXcg","28bBiMijfxXzJg8QFlRD9S","3LlVKDwVvfKgmg3fuO5Hmn","0I59iRPHvNyiXyJcBEMzrb","7hTbL8DerUDoZWW0ldnxIW","1hxQBvCt7kp9MuO5UFT6II","3d80267zr5AVMCOGPH1oQI","4DIYem4oT26j3jCVltJhxV","7JTy7NbFTwDzefJxd49Lf1","3Gt2IDUmYKNX1QzVIdRfX8","4LQ8QqBmnwCBteHpRhLW0T","6UR0agO8xxMsypcAzWMyLw","4DwgTZKVw2KhraKGriODbh","0wvlSU8nZS0T5L6nyob9Bx","61vsZ9e6ZsOhZEVPiXPPaT","5ZIG6gzJtMBerOYv0vnoYG","5IESCAblbsYpt9hn8ttWS7","2a6Jy3ZonmWzTdUyUwDJqC","4xGCgLLnwkpheU1aVExAp7","0neakn4D4qu4ltRk7hSgDw","3CBQ3hxI4rDL0xXy7KPMVy","2BKYKhjOcPcKgV10X6N8Dc","00em9T09LEQc2BSJlAmFD1","1ljHlFwoi63HR3mM63uk5C","4CuuKFF0Dwt1rFwZCUqX6H","4v35AtL5xyLOz6gwAU1ZHl","5qZiyvc8tMk90qKI98dCvJ","41toTq72KSVI4LTOBpWWcR","2EV4OmbSja9m3bMhm5Ez9T","5qIOGqVK8vRMuJtDle0hOF","2r5nhgPtpuJZHuX4w5KXp3","3t2YLrAMAyd9ncERLYWTpW","4fSxk2719Bl4n2PNOgHNaK","7EKTm19QVU4T4gFT2Z0ud6","3C1w1I4bAH27wif71nC6O3","01x58VUASxBJosKK3RkNd8","7DKU7b9ZK4qcX8kphSb9sP","5JcNt7HIpQ3isJmibFfGNG","3DTsSymVQGS95ezGecUj6S","27ffshxlJ4jdx51kimi47D","5BchHEvhIwR4f0OoyBhN0R","57sr5VBmlvg01nlpvMGypE","3pcpEvOH24KPbIaZgubPDk","4IZxUeSjAYL5jc3vniVRCF","03FTCjYriLaKJHgXYoB4w4","5CX9QapBUgSUqqo99o4N5x","6FNIOGEgIbkMgCEQ18CD4L","66aTopxt6f89xZ12CdLcml","2SIgrUmF8kmOhCiLQtBgU8","3eDaW0xG4uy0ePVY2dxwkh","44fx0FmOySciFTRhfVe3Im","6rsLENQb9Nhl4vwDkpPTcm","48e8hh6Svj4iSmHmzrXGAu","1pl2KyuxVQ5zawrx6MEukl","5ReRK2jIntojU5lDL1iHVH","73L5ra6svNJZ5wOroEN91B","1RhFh6tAyz7dE6JN30fyLr","70TonO1RTZlOUJOPUDUls7","1JvRXpptB1ow8IlCVjz055","3bHZLerTrV9dLAFq9hVWU0","665gLQpMp1cE6VcwRQs1AK","2VpNThxLkuOmBOLWvusyHx","3IQwmTSo2HUoITQ83d5T8r","1fCJfMRbFbsXmNSpjSHzzh","5pS9n3tQqFVlfXyLpl7UiV","3wubMIoyjl9fzEfO8QkyvP","6JQAf74Gmu6jEoLB51eFxY","6qgVHMomKTfMY5FU1pG3JU","1qPRF8lp82WDUEvCw9lbgZ","1jRXENGtJCw4e2yGK70JMC","75DB5zFYXRDYLKO5OPNirK","6SezFB3ekNmveVnTuiToV6","0xvxEyd7TiG1wYCcxIBayF","091Dv31T5TgwGNrdqFWhBl","4kUhaxY1jJ6RnaquhfM1BZ","2w2HXYYD5tqFBNuMaro7sI","2jIiSj2ZFJQjF0Dr3hKaKr","1Bi23brRTBv0YfrrTYeaPC","6I8w44uLed36NQdYQk4tnO","68w4AyxnlbmPyrTJCQsL6I","0br46jGMWHcKxhwDHYGYBX","3ZVbI2uvzs6bOzT0oladYS","1R6jJDOitsRJR9DgHraZ7m","2bDKtXRdF2ja1QOIce3vqK","4MEUUyupDo99GmGJOc8f0y","0YnBgV64YFXDXbybxgOldS","6uVQyJUQYLd2u52ZNeNd2W","5QOZzj6Mm859qmMXwf0t5G","05yZDnCh021UNDI1T58fD0","0q3aNtjtbxyXPCZo44Y6z9","7g6iJjDSCWfkfBTsLXwG2o","4SXn6G07QVKsPpqKEwzZhL","3aeHwPAyOzdOE8PVmBs5Hp","7w0wqMsxa6FoOqbhIBAPTM","1ABOHodyPVh2KKBWh1r9n2","2apYmxuqhDjSwDiwTdCDrV","61hAFUkwtoF5ayUHkMDTYo","7tc0QjRqLHpoxRdkZBJRT9","7anr7l73lU0melg0VBd2qW","18U3sVLeKjFHRYfYgaxWkU","5gKACzX59LuTwKo2cuSbSq","5nPPuTRehLe75ttupFW3YJ","2YSeuojJg0vk3UTmstKM3u","1qJiWpfaUf3rIziyUII2Ri","56ZuNp2g3Zg98CuqtLSzy5","5qwA9AJHCcBKv0HlOZIXsx","0GTAc30NpHYckkSZgOQJYA","7Eta0HDcWmZqwfukPBXxHO","4KU8iNeYB0kiiUKlfDeYFr","1Edvckz375Jb97XDzE9hUh","1hpD3OJuuUsNiQmLZ5xweq","4lEWybid2rTgjwbPZAIvdb","4aLruGmlOGnHNqIZe1fjeu","2zb3DPFJwiWlpgqQItRzhZ","742s9AwUo1j8rqaFqp6mu3","2oCfXLVHu8FhkQuc0QIqjb","5iCItf0RRzuokybdrF6THY"]

# ----------------------------------------------------------------

num_search_ids = len(search_ids)
print(f"Getting info for {num_search_ids} playlists.")
print("-------------------------------------------------------------------------------------")

#tracker for progress
playlist_count = 1

all_playlists = []
for playlist in search_ids:
    # Gets the base metadata for the playlist
    get_playlist_url = f"https://api.spotify.com/v1/playlists/{playlist}"
    playlist_res = requests.get(url=get_playlist_url, headers=headers)
    playlist_json = playlist_res.json()  

    #for printing status
    playlist_name = playlist_json['name']
    playlist_owner = playlist_json['owner']['display_name']  
    print(f"{playlist_name} by {playlist_owner} ({playlist_count}/{num_search_ids})")
    print(f"{playlist_json['external_urls']['spotify']}")

    #initial request for the track listings
    get_playlist_tracks_url = f"https://api.spotify.com/v1/playlists/{playlist}/tracks"
    playlist_items_res = requests.get(url=get_playlist_tracks_url, headers=headers)
    playlist_items_json = playlist_items_res.json()

    #retrieving additional pages if there are over 100 songs on a playlist
    playlist_tracks_request_urls = [get_playlist_tracks_url]
    next_page_url = playlist_items_json['next']
    while next_page_url is not None: 
       playlist_tracks_request_urls.append(next_page_url)
       next_page_request = requests.get(url=next_page_url, headers=headers)
       next_page_json = next_page_request.json()
       next_page_url = next_page_json['next']

    print(f"There are {len(playlist_tracks_request_urls)} page(s) of tracks for this playlist. Getting info now...")
    
    track_page = []
    counter=1
    #pulling track lists for every page of requests
    for request_url in playlist_tracks_request_urls:
        
        playlist_tracks_res = requests.get(url=request_url, headers=headers)
        playlist_tracks_json = playlist_tracks_res.json()
        
        tracks = []
        
        for item in playlist_tracks_json['items']:
            #only pulls the item if the track is valid
            if item['track'] is not None:
                artist_list = []
                for artist in item['track']['artists']:
                    artist_dict = {
                        "name" : artist['name'],
                        "id" : artist['id']
                    }
                    artist_list.append(artist_dict)
                track_dict = {
                    "track_name" : item['track']['name'],
                    "track_id" : item['track']['id'],
                    "artists" : artist_list
                }
                tracks.append(track_dict)
        
        playlist_page = {
            "request_page" : counter,
            "tracks" : tracks
        }

        print(f"    Page {counter} done.")

        track_page.append(playlist_page)
        counter +=1 
    
    #full entry for each playlist, including metadata and track info
    playlist = {
        "playlist_name" : playlist_name,
        "playlist_description" : playlist_json['description'],
        "playlist_owner" : {
            "owner" : playlist_owner,
            "id" : playlist_json['owner']['id']
        },
        "followers" : playlist_json['followers']['total'],
        "playlist_url" : playlist_json['external_urls']['spotify'],
        "playlist_id" : playlist_json['id'],
        "total_tracks" : playlist_tracks_json['total'],
        "tracks" : track_page
    }

    print("-------------------------------------------------------------------------------------")
    all_playlists.append(playlist)
    playlist_count += 1

#write the entire dataset into one json
with open(f"data/bedroom_pop_playlists.json", "w") as write_file: 
    json.dump(all_playlists, write_file, indent=2)

print("Done!")
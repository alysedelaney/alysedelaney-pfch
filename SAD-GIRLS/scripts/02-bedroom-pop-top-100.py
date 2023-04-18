import json
from collections import Counter

# =========================================================================

# Gets top 100 most frequent artists in the bedrooom pop playlists. 

# =========================================================================

artist_names = []

# add all artists names found in bedroom pop playlists to a json file
with open("data/bedroom_pop_playlists.json") as file:
    json_file = json.load(file)
    artist_counter = 1
    for playlist in json_file:
        for results_page in playlist['tracks']:
            for song in results_page['tracks']:
                for artist in song ['artists']:
                    artist_names.append(artist['name'])

#count each of the occurences of the artist and sort it
artist_count = dict(Counter(artist_names))
artist_count_sorted = dict(sorted(artist_count.items(), key=lambda x:x[1], reverse=True))

#pull the top 100 artists
top_100 = dict(list(artist_count_sorted.items())[0:100])
artists_100 = list(top_100.keys())

#print the list
print(artists_100)

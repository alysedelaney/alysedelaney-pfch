import json

track_data = []

with open('remaining-track-data.json') as track_file:
    track_json = json.load(track_file)

    for entry in track_json:
        for track in entry:
            title = track['name']
            track_id = track['id']
            preview_url = track['preview_url']
            spotify_url = track['external_urls']['spotify']
            explicit = track['explicit']
            popularity = track['popularity']

            track_dict = {
                "track_id" : track_id,
                "title" : title,
                "preview_url" : preview_url,
                "spotify_url" : spotify_url,
                "explicit" : explicit,
                "popularity" : popularity
            }

            track_data.append(track_dict)

print(json.dumps(track_data, indent=2))

with open('remaining-track-features.json') as features_file:
    features_json = json.load(features_file)

    for entry in features_json:
        for track in entry:
            track_id = track['id']
            track_danceability = track['danceability']

            track_data[track]
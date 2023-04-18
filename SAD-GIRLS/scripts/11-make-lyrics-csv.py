import json
import csv 

# =========================================================================

#

# =========================================================================

lyrics_file = open('data/csv_files_for_analysis/lyrics.csv', 'w')
csv_writer = csv.writer(lyrics_file)

headers = {
    "artist_name" : "artist_name",
    "artist_id" : "artist_id",
    "title" : "title",
    "track_id" : "song_id",
    "description" : "description",
    "lyrics" : "lyrics",
    "hot" : "hot"
}

csv_writer.writerow(headers.values())

with open('data/compiled_song_info.json') as read_file:
    json_file = json.load(read_file)

    for entry in json_file:
        artist_name = entry['artist_name']
        artist_id = entry['spotify_id']

        for song in entry['songs']:
            title = song['title']
            song_id = song['spotify_id']
            description = song['description']
            lyrics = song['lyrics']
            hot = song['hot']

            song_dict = {
                "artist_name" : artist_name,
                "artist_id" : artist_id,
                "title" : title,
                "track_id" : song_id,
                "description" : description,
                "lyrics" : lyrics,
                "hot" : hot
            }

            csv_writer.writerow(song_dict.values())

lyrics_file.close()

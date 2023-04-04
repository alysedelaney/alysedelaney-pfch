import json

with open("all-related-artists.json") as file:
    json_file = json.load(file)
    for entry in json_file:
        print(entry['name'])
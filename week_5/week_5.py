import json

nat_dict = {}

with open('Artworks.json') as file: 
    json_file = json.load(file)
    #counter to see progress
    # count = 1
    for artwork in json_file: 
        list_nat = artwork['Nationality']
        #removes duplicate nationalities from each list
        list_nat = list(dict.fromkeys(list_nat)) 
        for nat in list_nat: 
            if nat in nat_dict: 
                nat_dict[nat].append(artwork)
            else: 
                nat_dict[nat] = [artwork]
        #Only print counter divisible by 500
        # if count % 500 == 0:
        #     print(count)
        # count = count + 1 
    
for nat_key in nat_dict: 
    with open(f"res/{nat_key}.json", 'w') as write_file:
        json.dump(nat_dict[nat_key],write_file,indent=2)
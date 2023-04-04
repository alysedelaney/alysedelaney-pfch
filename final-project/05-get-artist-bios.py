import lyricsgenius
import json
import time
import re

#--API Setup------------------------------------------

user_token = "HA_bejJPPswn7Oi-ehqP-q9Ka2kkqJDppHjWSuXC4eyaVUYkaYQyR-xV-6FJXTnj"
genius = lyricsgenius.Genius(user_token,sleep_time=0.5,timeout=5, retries=3)

#--*** Search Input Here ***--------------------------

all_artist_names = ["Joy Crookes", "Joy Williams", "Julia Holter", "Julia Jacklin", "Julien Baker", "Kate Bollinger", "Katie Gregson-MacLeod", "Katy Kirby", "Kelsey Lu", "Kilo Kish", "King Princess", "Kississippi", "Kita Alexander", "Lady Lamb", "Lala Lala", "Laura Elliott", "Laura Stevenson", "Lauren Aquilina", "Lauren Sanderson", "Lauren Weintraub", "Lava La Rue", "Leith Ross", "Lennon Stella", "Lexi Jayde", "Liza Anne", "Lizzy McAlpine", "Lomelda", "Long Beard", "Lucy Dacus", "Lydia Luce", "Maddie Zahm", "Madeline Kenney", "Madison McFerrin", "Maggie Rogers", "Maisie Peters", "Mallrat", "Margaret Glaspy", "Matilda Mann", "Maude Latour", "Meg Mac", "Mereba", "MIA GLADSTONE", "Mia Joy", "Miel", "Mitski", "Miya Folick", "ML Buch", "Molly Burch", "Molly Parden", "MUNA", "mxmtoon", "Natalie Prass", "NERIAH", "Nilüfer Yanya", "Oh Pep!", "Okay Kaya", "Olive Klug", "Orion Sun", "Orla Gartland", "P.S. Eliot", "Palehound", "Penelope Scott", "Phoebe Bridgers", "Pip Millett", "quinnie", "Raveena", "Ravyn Lenae", "Remi Wolf", "Reneé Rapp", "Rico Nasty", "ROSIE", "Rosie Carney", "Rosie Darling", "Rosie Tucker", "Ruby Fields", "Salami Rose Joe Louis", "Samia", "SASAMI", "Shannon Lay", "Sharon Van Etten", "Sidney Gish", "Skullcrusher", "Snail Mail", "Soccer Mommy", "Sody", "Solange", "Sophie Holohan", "spill tab", "Squirrel Flower", "St. Vincent", "Stella Donnelly", "Sudan Archives", "Suki Waterhouse", "Tanukichan", "Taylor Acorn", "Taylor Bickett", "Tenci", "Tessa Violet", "The Aces", "The Japanese House", "The Staves", "The Wild Reeds", "Tia Gostelow", "Tierra Whack", "Tirzah", "Tkay Maidza", "Tomberlin", "Tommy Lefroy", "U.S. Girls", "UMI", "Vagabon", "Vera Blue", "VÉRITÉ", "Wallice", "Waxahatchee", "Whatever, Dad", "WILLOW", "Wilma Laverne Miner", "Yazmin Lacey", "Zeph", "Zolita"]

# completed = ["Abby Sage", "Ada Lea", "Adrianne Lenker", "Aldous Harding", "Alex Lahey", "Alex the Astronaut", "Alexa Cappelli", "Alice Phoebe Lou", "Allie Crow Buckley", "Ana Roxanne", "Andrea von Kampen", "Angel Olsen", "Angie McMahon", "Annie DiRusso", "Aoife O'Donovan", "Arlo Parks", "Ashe", "Ashley Kutcher", "Avery Lynch", "awfultune", "Baby Queen", "Barrie", "beabadoobee", "Beach Bunny", "Becca Mancari", "Bedouine", "BENEE", "Betty Who", "Biig Piig", "Black Belt Eagle Scout", "Blondshell", "Blu DeTiger", "BLÜ EYES", "boygenius", "Boyish", "Bree Runway", "Bully", "Buzzy Lee", "Caitlin Rose", "carobae", "Caroline Rose", "Caroline Spence", "Cassandra Jenkins", "Cate", "Cate Le Bon", "Cavetown", "Chappell Roan", "Charlotte Cornfield", "Charlotte Day Wilson", "chloe moriondo", "Chloe x Halle", "Clairo", "Claud", "Cleo Sol", "Coco & Clair Clair", "Cornelia Murr", "Courtney Marie Andrews", "Daisy the Great", "Delaney Bailey", "Devon Again", "Discovery Zone", "dodie", "Doechii", "Dora Jar", "Dreamer Isioma", "Eleanor Friedberger", "ella jane", "Emily James", "Empress Of", "Erin Rae", "Esmé Patterson", "Ethel Cain", "fanclubwallet", "Faye Webster", "Fazerdaze", "FELIVAND", "Fenne Lily", "FKA twigs", "FLETCHER", "Flower Face", "Frankie Cosmos", "Freak Slug", "Free Cake For Every Creature", "Gatlin", "Genevieve Stokes", "Gia Margaret", "girl in red", "girlhouse", "girlpuppy", "Gloria Laing", "Grace Gaustad", "Grace Ives", "Greta Isaac", "Gretta Ray", "Haley Blais", "Haley Heynderickx", "Haley Joelle", "Hana Vu", "Hand Habits", "Hannah Cohen", "Hatchie", "Hazel English", "Helena Deland", "Hey Cowboy!", "Hope Tala", "Hurray For The Riff Raff", "Indigo De Souza", "Indigo Sparke", "Ira Wolf", "Jack River", "Jade Bird", "Jana Horn", "Japanese Breakfast", "Jay Som", "Jenny Lewis", "Jess Williamson", "JESSIA", "Jessica Pratt", "JGrrey", ]
 
 # failed = ["illuminati hotties", "Jordana", "JOSEPH", ]

counter = 1
total_search = len(all_artist_names)

for artist in all_artist_names:
    
    artist_info = []
    artist_file = re.sub('[^A-Za-z0-9]+', '', artist).lower()

    print(f"------------ {counter}/{total_search} ------------------------------------")
    #--Setting up the request-----------------------------
    song_limit = 1 #just to verify this is the correct artist, check against pulled songs, can increase or decrease
    artist_data = genius.search_artist(artist,max_songs=song_limit)

    if artist_data is not None:

        #--Create Dictionary from results---------------------
        artist_dict = artist_data.to_dict()
        alt_name = artist_dict['alternate_names']
        desc = artist_dict['description']
        artist_id = artist_dict['id']
        artist_image_url = artist_dict['image_url']
        insta = artist_dict['instagram_name']
        name = artist_dict['name']

        artist_dict_short = {
            "name" : name,
            "id" : artist_id,
            "instagram_name": insta,
            "alternate_names" : alt_name,
            "description" : desc,
            "image_url" : artist_image_url,
        }

        artist_info.append(artist_dict_short)
        time.sleep(1)
    
    with open(f"data/artist_info/{artist_file}_artist_info.json", "w") as write_file:
        json.dump(artist_info, write_file, indent=2)

    print(f"========== {artist} file written. ==========")

    counter += 1
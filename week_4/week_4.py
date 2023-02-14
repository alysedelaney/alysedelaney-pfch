import csv

#create empty dictionary
nationality_dict = {}

#open Artworks.csv
with open('Artworks.csv') as file: 

    #read Artworks.csv
    artworks_processed = csv.reader(file)
    #add header info to a variable
    header_row = next(artworks_processed, None)

    for row in artworks_processed: 
        #pull the nationalities column
        nationalities_unsplit = row[4]
        #and split it at each space
        nationalities = nationalities_unsplit.split(' ')

        for nationality in nationalities: 

            #if the nationality has already been added to the dictionary 
            if nationality in nationality_dict: 
                nationality_dict[nationality]['csv'].writerow(row)

            else: 
                #opens a new file in the specified path with the nationality's name
                nationality_file = open(f"res/{nationality}.csv", 'w')
            
                #writes to the created file
                nationality_csv = csv.writer(nationality_file)
            
                #writes the header to the file
                nationality_csv.writerow(header_row)
            
                #writes each row for that nationality
                nationality_csv.writerow(row)

                nationality_dict[nationality] = {
                    'file': nationality_file,
                    'csv': nationality_csv
                }
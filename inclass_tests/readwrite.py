import csv

# with open("my_file.txt", 'w') as my_file:
#   my_file.write("hello\n")
#   my_file.write("world\n")
#   my_file.write("all of these are on their own line because of the \\n \n")

# with open("my_file.txt", 'r') as my_file:
#   for line in my_file:
#     print(line)

# with open('10014_abridged.csv') as file:
#   processed_csv = csv.reader(file)
#   for row in processed_csv:
#     print (f"{row[7]} was built in {row[18]} and is owned by: {row[14]}")
#     print("--------------------------------------------------------------------")


# with open('10014_abridged.csv') as file:
#   processed_csv = csv.DictReader(file)
#   first_line = next(processed_csv, None)
#   for row in processed_csv:
#     if row['yearbuilt'] == '1915':
#         print(f"{(row['address']).title()}, New York, NY {row['zipcode']}")


with open('10014_abridged.csv') as file:
  with open('date_1907.csv', 'w') as write_file: 
    processed_csv = csv.reader(file)
    write_csv = csv.writer(write_file)
    header = next(processed_csv, None)
    write_csv.writerow(header)
    for row in processed_csv: 
      if row[18] == '1907':
        write_csv.writerow(row)
        print(row)
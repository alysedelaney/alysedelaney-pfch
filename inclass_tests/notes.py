dictionary = {
'NY': 'New York',
'NJ': 'New Jersey',
'MN': 'Minnesota',
'codes': ['NY','NJ','MN'],
'pop': {
  'NY': 19.84,
  'NJ': 9.27,
  'MN': 5.71
}
}

for key in dictionary:
    value = dictionary[key]
    if type(value) is str:
        print(f"{key} is {value}")
    elif type(value) is list:
        for x in value: 
            print(x)
    elif type(value) is dict:
        for x in value: 
            print(f"{dictionary[x]} has a population of {value[x]}")
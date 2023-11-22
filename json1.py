import json


data = {

    'name': 'Luam Redai',
    'age': 24,
    'city': 'Virginia, USA',
    'interests': ['Read','Exercise','Travel'],
    'is student': True
}
#write down json data file
with open('data.json', 'w') as json_file:# w =writing
    json.dump(data, json_file, indent=4)#4 move further with json.dump
    print ('Data written to data.json')#confirm
    

with open ('data.json', "r") as json_file:# R=reading from the file
    loaded_data = json.load(json_file)# creating a json file loading
    print ('Data loaded form data. json:')
    print (loaded_data)


#data creation for value pairing 
loaded_data['age'] = 24
#append with correct key
loaded_data['interests'].append("I'm a ninja")
#adjust statement in the json file                               


with open('data.json', 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)
    #confirm printing
    print('modified data to data.json file')

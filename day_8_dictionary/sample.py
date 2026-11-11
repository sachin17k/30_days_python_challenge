person = {
    'name':'sachin',
    'age':20,
    'country':'india',
    'degree':'aiml',
    'skills':['python','java','html','css']
    }

print(f"number key value pairs in the dictionary: {len(person)}")
print(person['name'])
print(person['age'])
#print(person['city']) #throws error

# get() method

print(person.get('skills'))
print(person.get('city')) #prints none object data type

# adding items in a dictionary
person['city']='tirunelveli'

# adding a items in the list which is inside the dictionary
person['skills'].append('github')

print("dictionary after changing ",person)

# modifying items 
person['name'] = 'kumar'
print("after modifying:",person)

# checking keys exist in the dictionary
print('name' in person)
print('city' in person)
print('skills'  in person)
print('village' in person)

# removing keys ,values pairs in the dictionary 
#1 pop()
person.pop('age')
print(person)

#2 popitem removes last item 
person.popitem()
print('person')

#3 del
del person['degree']

# creating the dictionary into list of tuples
dict_list = person.items()
print(dict_list)

# clearing and deleting dictionaries

dict1 = {'name':'sachin'}
dict2 = {'age':20}

print(dict1.clear())
del dict2
# print(dict2) 3 throws name error
# coping a dictionary 
person_copy = person.copy()
print("copy :\n",person_copy)

# getting dictionary keys as list
key = person.keys()
print("key :",key)

# getting dictionary values as list
v = person.values()
print("values:",v)
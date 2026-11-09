student = {
    'name' : 'Sachin',
    'age' : 20,
    'city' : 'tirunelveli'
}

for index , key in enumerate(student):
    print(index, key)

for index , (key,value) in enumerate(student):
    print(index, key, value)
    
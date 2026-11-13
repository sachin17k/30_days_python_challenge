#range
print("range")
lst = list(range(11))
for i in lst:
    print(i)

#nested for loop
print("nested for loop")
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for s in person['skills']:
            print(s)

#for .... else
print("for...else")
num = list(range(11))
for i in num:
    print(i)
else:
    print("the loop exits when the number is :",i)

#pass
print("pass")
for i in range(1,10,2):
    pass
#pass is a place holder , performs no action
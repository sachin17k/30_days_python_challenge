#for loop for list 
print("for loop in list")
num =[1,2,3,4,5,6,7]
for n in num:
    print(n)

# for loop for string
print("for loop in string")
str = 'sachin'
for s in str:
    print(s)

#for loop for tuple 
print("for loop in tuple")
tpl = (1,2,3,4,5)
for t in tpl:
    print(t)

#for loop for set
st = {1,2,3,4,5,6,7,8,9,10}
print("for loop in set")
for i in st:
    print(i)

#for loop in dictionary
print("for loop in dictionary")
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

#for extracting keys
for key in person:
    print(key)

# for extracting keys and values 
for key , value in person.items():
    print(key,value)
#creating a module file with more functiona and datatypes 

def greeting(name):
    return 'Welcome, '+ name

def sum_all(*nums):
    total = 0
    for i in nums:
        total += i
    return total

gravity = 9.81
person = {
    'name' :'sachin',
    'city': 'Tirunelveli'
    }
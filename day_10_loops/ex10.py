#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
n = len(fruits)-1
while True:
    print(fruits[n])
    n -= 1
    if n == -1:
        break 
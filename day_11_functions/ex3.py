#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lst):
    return lst[::-1]
num = [9,8,7,6,5,4,3,2,1]
result =reverse_list(num)
print(result)

#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def cap(x):
    s = ''.join(x).upper()
    return s.split()
n = ['s','a','c','h','i','n']
print(cap(n))
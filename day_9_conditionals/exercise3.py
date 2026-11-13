'''Get two numbers from the user using input prompt. 
If a is greater than b return a is greater than b,
if a is less b return a is smaller than b, else a is equal to b'''

#program
a = int(input("Enter a number :"))
b = int(input("Enter a number :"))
if a > b:
    print(a,"is greater than ",b)
elif a < b:
    print(a, "is smaller than", b)
else:
    print("a is equal to b")
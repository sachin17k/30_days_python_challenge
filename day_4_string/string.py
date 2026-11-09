#string concatenation
a='sachin'
b=' kumar'
c=a+ b
print(c)

#escape sequence
print("hii guys , iam sachin kumar. \n Iam from Tirunelveli.")
print("sachin \t kumar \t lily")
print("5 \t 5 \t 10")
print("printing backslash: \\")
print("printing quotes \' \" ")

#string formatting
#old style
name = 'sachin'
age = 20
percentage = 95.555
print("i'm %s, my age is %d, my percentage is %.2f"%(name,age,percentage))

#new method in python 3
print("im {}, my age is {}, my percentage is {} , {}".format(name,age,percentage,percentage))

#advanced method 
print(f"Im {age}, my age is {name}, my percentage is {percentage},{percentage:.2f}")
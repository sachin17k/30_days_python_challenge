'''Compare the values of my_age and your_age using if … else. 
Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
 You can use a nested condition to print 'year' for 1 year difference in age,
  'years' for bigger differences, and a custom text if my_age = your_age'''

#program
my_age = 20
your_age = int(input("Enter your age: "))

if my_age > your_age:
    print(f"iam older than you, the difference in age is {my_age - your_age}")
elif my_age < your_age:
    print(f"your are older than me , the difference in age is {your_age - my_age}")
else:
    print("we two are in same age")
#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum =0
for i in range(101):
    sum = sum +i
print(f"The sum of 0 to 100 is {sum}")

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

s =0
for i in range(0,101,2):
    s = s +i
print(f"The sum of all even numbers from 0 to 100 is {s}")

n =0
for i in range(1,101,2):
    n = n +i
print(f"The sum of all odd numbers from 0 to 100 is {n}")
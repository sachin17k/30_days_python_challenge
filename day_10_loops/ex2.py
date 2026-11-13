#Iterate 10 to 0 using for loop, do the same using while loop.
print("FOR LOOP")
num = list(range(11))
rev = num[::-1]
for i in rev:
    print(i)

print("WHILE LOOP")
count = 10
while count >=0:
    print(count)
    count-=1
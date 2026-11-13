# break and continue in for loop
print("break:")
num = [1,2,3,4,5,6,7]
for n in num:
    if n==3:
        break
    print(n)

# continue in for loop
print("continue:")
for i in num:
    if i == 3:
        continue
    print(i)
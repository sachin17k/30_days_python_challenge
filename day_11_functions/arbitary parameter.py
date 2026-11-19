#if we dont know the no. of args we pass we use arbitary parameters by using (*)
def add_all(*num):
    total = 0
    for i in num:
        total+= i
    return total
print(add_all(2,7,8,9,55,45))
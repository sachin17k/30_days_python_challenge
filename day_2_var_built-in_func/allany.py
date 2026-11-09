marks = [36,33,60,77,80,100]
all_pass = all(x>=35 for x in marks)
print(f"All passed:{all_pass}")
centum = any(x==100 for x in marks)
print(f"Centum:{centum}")
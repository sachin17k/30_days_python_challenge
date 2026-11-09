s = list(input("Enter the string to be reversed: "))
m = int(input("Enter  method 1 or 2 :"))
if m == 1:
    s.reverse()
    final = ''.join(s)
    print(f"Reversed string :{final}")
else:
    s1 = ''.join(s)
    rev = s1[::-1]
    print(f"Reversed string :{rev}")
#unpacking characters
lang = 'python'
a,b,c,d,e,f = lang
print(a)
print(b)
print(f)

#accessing characters
first_letter = lang[0]
last_letter = lang[5]
last_letter2 = lang[-1]

#slicing

print(lang[0:3])
print(lang[3:])
print(lang[-3:])
print(f"1st method: {lang[0:6:2]},2nd method {lang[::3]}")
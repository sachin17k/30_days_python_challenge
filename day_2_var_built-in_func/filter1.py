names = ["Sachin", "", "Rahul", "", "Amit",9]

result = filter(lambda name: len(name) > 0, names)

print(list(result))
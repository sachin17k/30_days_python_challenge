def square(x):
    if isinstance(x,(int,float)):
        return x*x
    return "Invalid Input"
print(square(5))
print(square('hello'))
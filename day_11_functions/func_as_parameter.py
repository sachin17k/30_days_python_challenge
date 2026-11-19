#You can pass functions around as parameters
def square(n):
    return n ** n
def do(do,x):
    return do(x)
print(do(square,5))
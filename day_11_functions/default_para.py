#default parameter if we dont pass any args
def greet(name="sachin"):
    msg = 'welcome, '+name
    return msg
print(greet())
print(greet('tamil'))
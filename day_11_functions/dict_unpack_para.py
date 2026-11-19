def greet(name,location):

    print("hii,Iam "+ name +" from "+ location)

my_dict = {
    'name':'sachin',
    'location':'nagercoil'
}
greet(**my_dict)
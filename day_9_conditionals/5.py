'''fruits = ['banana', 'orange', 'mango', 'lemon']

If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
If the fruit exists print('That fruit already exist in the list')'''

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter the fruit: ")
if fruit.lower() in fruits:
    print(fruit,"fruit already exist in the list")
else:
    print(fruit,"doesn't exist in the list")
    fruits.append(fruit)
    print(fruits)


while True:
    num_1 = int(input("Enter 1st number: "))
    num_2 = int(input("Enter 2nd number: "))

    op = int(input("""
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Floor Division
    6. Modulus (Remainder)
    7. Power
    8. Exit

    Select your operation: """))

    if op == 1:
        print(f"Addition: {num_1 + num_2}")

    elif op == 2:
        print(f"Subtraction: {num_1 - num_2}")

    elif op == 3:
        print(f"Multiplication: {num_1 * num_2}")

    elif op == 4:
        if num_2 == 0:
            print("Cannot divide by zero!")
        else:
            print(f"Division: {num_1 / num_2}")

    elif op == 5:
        if num_2 == 0:
            print("Cannot divide by zero!")
        else:
            print(f"Floor Division: {num_1 // num_2}")

    elif op == 6:
        if num_2 == 0:
            print("Cannot divide by zero!")
        else:
            print(f"Remainder: {num_1 % num_2}")

    elif op == 7:
        print(f"Power: {num_1 ** num_2}")

    elif op == 8:
        print("END OF CALCULATION")
        break

    else:
        print("Invalid operation!")

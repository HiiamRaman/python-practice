# practice calculator
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# 5. Exit
# Use try/except
# Handle ValueError
# Handle ZeroDivisionError
# Reject invalid menu options using raise ValueError(...)


def add():
    try:
        print("Function add is running ")
        val1 = int(input("Enter first  number "))
        val2 = int(input("Enter second number "))

        print(f"Sum is {val1+val2}")
    except ValueError:
        print("Enter valid Numbers ")


def sub():
    try:
        print("Subtraction function is running ")
        val1 = int(input("Enter first  number "))
        val2 = int(input("Enter second number "))
        print("subtraction value is ", val1 - val2)
    except ValueError:
        print("Enter valid Numbers ")


def multiply():
    try:
        print("Multiply function is running ")
        val1 = int(input("Enter first  number "))
        val2 = int(input("Enter second number "))
        print(" the value after multiplication is ", val1 * val2)
    except ValueError:
        print("Enter valid Numbers ")


def divide():
    try:
        print("Division function is running ")
        val1 = int(input("Enter first  number "))
        val2 = int(input("Enter second number "))
        print(" the value after division is ", val1 / val2)
    except ZeroDivisionError:
        print(" cannot divide by 0")
    except ValueError:
        print('Enter valid numbers ')


def calculator():
    try:
        option = int(input("Enter a option from 1-4"))
        if option == 1:
            add()
        elif option == 2:
            sub()
        elif option == 3:
            multiply()
        elif option == 4:
            divide()
        elif option == 5:
              print("Good bye ")
              
        else:
            raise ValueError(" chooose option between 1-5")
       
          

    except ValueError:
      print('Enter Valid options')
calculator()

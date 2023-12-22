# This is basic arithmatic calculator with Addition, Subraction, Multiplication, Division operations.
# Addition function
def add(x, y):
    return x + y

# Subtraction function
def subtract(x, y):
    return x - y

# Multiplication function
def multiply(x, y):
    return x * y

# Division function
def divide(x, y):
    return x / y

# Main calculator function
def calculator():
    print("Welcome to the calculator program!")
    while True:
        # Display the menu options
        print("Please select an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Thank you for using the calculator program!")
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print("The result is:", add(num1, num2))
        elif choice == '2':
            print("The result is:", subtract(num1, num2))
        elif choice == '3':
            print("The result is:", multiply(num1, num2))
        elif choice == '4':
            if num2 != 0:
                print("The result is:", divide(num1, num2))
            else:
                print("Error: Cannot divide by zero!")
        else:
            print("Invalid input! Please try again.")

# Call the calculator function
calculator()
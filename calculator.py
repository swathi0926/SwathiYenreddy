print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

try:
    select = int(input("Enter your choice (1-4): "))
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if select == 1:
        print("Addition is:", num1 + num2)

    elif select == 2:
        print("Subtraction is:", num1 - num2)

    elif select == 3:
        print("Multiplication is:", num1 * num2)

    elif select == 4:
        if num2 == 0:
            print("Error: cannot divide by zero")
        else:
            print("Division is:", num1 / num2)

    else:
        print("Invalid Selection. Please choose a number between 1 and 4.")

except ValueError:
    print("Invalid input! Please enter only numbers.") 

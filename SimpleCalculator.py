#A simple calculator python program that implements user input and output.

print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    operation = input("Enter choice (1/2/3/4): ")

    # addition code
    if operation == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("the addition is: " + str(float(num1) + float(num2)))

    # subtraction code
    elif operation == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("the subtraction is: " + str(float(num1) - float(num2)))

    # multiplication code
    elif operation == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("the product is: " + str(float(num1) * float(num2)))

    # division code
    elif operation == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            print("the division is: " + str(float(num1) / float(num2)))
        else:
            print("Error! Division by zero.")

    else:
        print("Invalid Input")

    # prompting for next calculation
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break

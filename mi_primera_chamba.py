# Maybe let's try doing something fun?
# A simple calculator!

Calculator = True

print("Welcome to basic calculator! Please select from the following list to begin \n" "1. Adition \n" "2. Subtraction \n" "3. Multiplication \n" "4. Division \n" "5. Exit \n")
while Calculator is True:
    type_of_operation = input(": ")
    try:
        type_of_operation = int(type_of_operation)
        if type_of_operation == 1:
            first_variable = int(input("Input first number: "))
            second_variable = int(input("Input second number: "))
            print(f"{first_variable} + {second_variable} = {first_variable + second_variable} ( ˶ˆᗜˆ˵ )")
            choice = int(input("Type 1 to go back or type 2 to finish: "))
            if choice == 1:
                continue
            elif choice == 2:
                break
        if type_of_operation == 2:
            print("Subtraction executed")
            first_variable = int(input("Input first number: "))
            second_variable = int(input("Input second number: "))
            print(f"{first_variable} - {second_variable} = {first_variable - second_variable} ( ˶ˆᗜˆ˵ )")
            break
        if type_of_operation == 3:
            print("Multiplication executed")
            first_variable = int(input("Input first number: "))
            second_variable = int(input("Input second number: "))
            print(f"{first_variable} * {second_variable} = {first_variable * second_variable} ( ˶ˆᗜˆ˵ )")
            break
        if type_of_operation == 4:
            print("Division executed")
            first_variable = int(input("Input first number: "))
            second_variable = int(input("Input second number: "))
            print(f"{first_variable} / {second_variable} ÷ {first_variable / second_variable} ( ˶ˆᗜˆ˵ )")
            break
        if type_of_operation == 5:
            print("Exit executed")
            break
    except ValueError:
        print("Please choose a interger.")
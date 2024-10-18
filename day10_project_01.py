# calculator

import day_10_project_01_logo as logo

def addition_two_numbers(num1, num2):
    return num1 + num2

def subtraction_two_numbers(num1, num2):
    return num1 - num2

def multiplication_two_numbers(num1, num2):
    return num1 * num2

def division_two_numbers(num1, num2):
    return round(num1 / num2, 2)


calculator_dictionary = {
    "+": addition_two_numbers,
    "-": subtraction_two_numbers,
    "*": multiplication_two_numbers,
    "/": division_two_numbers
}

def user_input(continue_operation, prev_answer):
    num1 = num2 = 0
    if continue_operation == 'n':
        while True:
            try:
                num1 = int(input("Enter first number: "))
            except ValueError:
                print("Invalid input")
                continue
            else:
                break
    else:
        num1 = prev_answer
        print("First number set to: ", num1, "\n")

    while True:
        operation = input(f"Choose operation: {', '.join(calculator_dictionary.keys())} ")
        if operation in calculator_dictionary:
            break
        else:
            print("Invalid operation")

    while True:
        try:
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input")
            continue
        else:
            break

    return num1, num2, operation

continue_calculator = True
continue_operation_str = 'n'
answer = 0

print(logo.logo)
while continue_calculator:
    print("Welcome to basic calculator!")
    print("\n")

    number1, number2, operation_symbol = user_input(continue_operation_str, answer)

    answer = calculator_dictionary[operation_symbol](number1, number2)
    print(f"{number1} {operation_symbol} {number2} = {answer}")

    user_choice = ''
    while user_choice not in ['y', 'n']:
            user_choice = (input("Do you want to continue? 'y' or 'n': ")).lower()
            if user_choice == 'y':
                continue_operation_str = input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
                if continue_operation_str not in ['y', 'n']:
                    print("Invalid input. starting a new calculation...")
                    continue_operation_str = 'n'
            elif user_choice == 'n':
                continue_calculator = False
            else:
                print("Invalid input")
                continue


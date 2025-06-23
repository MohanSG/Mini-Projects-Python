from calculator_art import art
import os

def calculate(n1, n2, operator):
    answer = 0
    if operator == "+":
        answer = n1 + n2
    elif operator == "*":
        answer = n1 * n2
    elif operator == "-":
        answer = n1 - n2
    elif operator == "/":
        answer = round(n1 / n2, 2)
    
    return answer

start_new_calcuations = True
while start_new_calcuations:
    print(art)
    number1 = int(input("What is the first number?: "))

    continue_calculating = True
    while continue_calculating:
        print("+\n-\n*\n/")
        operator  = input("Pick an operator: ")
        number2 = int(input("What is the second number?: "))
        answer = calculate(number1, number2, operator)

        print(f"{number1} {operator} {number2} = {answer}")
        go_again = input(f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation or 'exit' to stop:  ")

        if go_again == 'y':
            number1 = answer
        elif go_again == 'n':
            number1 = 0
            number2 = 0
            continue_calculating = False
            os.system('cls')
        elif go_again == 'exit':
            continue_calculating = False
            start_new_calcuations = False

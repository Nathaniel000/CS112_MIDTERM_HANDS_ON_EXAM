import random

def main():
    operation = input("Choose an operation (+, -, *, /): ")

    if operation not in ['+', '-', '*', '/']:
        print("Invalid operation. Please choose +, -, *, or /.")
        return

    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)

    user_answer = float(input(f"Solve the equation: {num1} {operation} {num2} = "))

    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    elif operation == '/':
        correct_answer = num1 / num2

    if user_answer == correct_answer:
        print("Congratulations! You are correct!\n")
        show_title_screen()

    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")

def show_title_screen():
    print("********************************************")
    print("*               Congratulations!            *")
    print("*           You've completed the task!      *")
    print("********************************************")

if __name__ == "__main__":
    main()

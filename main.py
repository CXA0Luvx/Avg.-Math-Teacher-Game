import random

OPERATORS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: round(x / y, 2)
}

def ask_question():
    operator = random.choice(list(OPERATORS.keys()))
    num1, num2 = random.randint(1, 9), random.randint(1, 9)
    answer = OPERATORS[operator](num1, num2)
    user_answer = float(input(f"What is {num1} {operator} {num2}? "))
    return abs(user_answer - answer) < 0.0001

def play_game():
    print("Welcome! I will ask you questions until you get one wrong. Earn as many points as you can.")
    points = 0
    while ask_question():
        points += 1
    print("Good game!")
    print(f"You earned {points} point{'s' if points != 1 else ''}.")
    
if __name__ == "__main__":
    play_game()

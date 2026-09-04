import random

OPERATORS = ['+', '-', '*', '/']
MIN_OPERAND = 3
MAX_OPERAND = 12


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    # Ensure no division by zero
    if operator == '/':
        while right == 0:
            right = random.randint(MIN_OPERAND, MAX_OPERAND)

    problem = f"{left} {operator} {right}"
    return problem


# Number of questions
TOTAL_QUESTIONS = 5

score = 0

print("Welcome to the Math Quiz!")
print(f"You will get {TOTAL_QUESTIONS} questions.\n")

for question_number in range(TOTAL_QUESTIONS):
    problem = generate_problem()

    # Calculate the correct answer
    answer = eval(problem)

    while True:
        user_answer = input(
            f"Question {question_number + 1}: {problem} = "
        )

        try:
            user_answer = float(user_answer)
            break
        except ValueError:
            print("Please enter a valid number.")

    if user_answer == answer:
        print("Correct! 🎉\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {answer}.\n")


print("Quiz finished!")
print(f"You got {score}/{TOTAL_QUESTIONS} correct.")
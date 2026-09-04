import time
import random

sentences = [
    "Python is easy to learn.",
    "I am learning programming.",
    "Practice makes you better.",
    "Coding is a useful skill."
]

while True:
    sentence = random.choice(sentences)

    print("\nType this sentence:")
    print(sentence)

    input("\nPress Enter when you are ready...")

    start_time = time.time()

    user_input = input("\nType here: ")

    end_time = time.time()

    time_taken = end_time - start_time

    words = len(user_input.split())
    wpm = words / (time_taken / 60)

    print(f"\nTime: {time_taken:.2f} seconds")
    print(f"WPM: {wpm:.2f}")

    again = input("\nTry again? (y/n): ")

    if again.lower() != "y":
        break
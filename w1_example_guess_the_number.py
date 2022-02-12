# Game "Guess the number"

import random

number = random.randint(0, 101)

while True:
    answer = input("Enter a number from 0 to 100: ")
    if not answer or answer == "exit":
        break

    if not answer.isdigit():
        print("Enter a correct number!")
        continue

    user_answer = int(answer)

    if user_answer > number:
        print("Guessed number is less.")
    elif user_answer < number:
        print("Guessed number is bigger.")
    else:
        print("Correct answer!")
        break

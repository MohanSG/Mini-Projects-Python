import random
import os
from guess_art import art

random_number = random.randint(1, 100)
guess_count = 0
max_guesses = 0

os.system('cls')

def check(num, answer):
    if num > answer:
        print("Too high")
        return False
    elif num < answer:
        print("Too low")
        return False
    else:
        return True

print(art)
print("Welcome to the Number Guessing Game!")
difficulty = input("Choose a difficulty. 'easy' or 'hard: ")

if difficulty == "hard":
    guess_count = 5
    max_guesses = 5
elif difficulty == "easy":
    guess_count = 10
    max_guesses = 10

in_play = True
while in_play:

    print(f"You have {guess_count} attempts to guess the number")

    guess = int(input("Make a guess: "))
    if check(guess, random_number):
        print(f"Congratulations! You guessed the number {random_number} in {max_guesses - guess_count} guesses!")
        in_play = False
    else:
        guess_count -= 1

    if guess_count < 1:
        print("You have run out of lives!")
        in_play = False
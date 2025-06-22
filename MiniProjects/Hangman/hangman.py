import random
from hangman_art import game_art
from hangman_words import word_list

word = random.choice(word_list)

word_length = len(word)

guessed_letters = ["_"] * word_length
correct_guesses = 0

game_over = False

lives = 6

print(game_art[6])
print(''.join(guessed_letters))

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess not in guessed_letters:
        for letter in range(len(word)):
            if word[letter] == guess:
                correct_guesses += 1
                guessed_letters[letter] = guess
    else:
        print(f"{guess} has already been guessed")
        
    if guess not in word:
        lives -= 1
        print(game_art[lives])
        print(f"{guess} is not correct, you lose a life")

    print(''.join(guessed_letters))

    if correct_guesses == word_length:
        game_over = True
        print("**********You win!**********")
    elif lives == 0:
        game_over = True
        print("**********You lose!**********")
        print(f"The word was {word}")
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_choices = ["rock", "paper", "scissors"]
game_art = [rock, paper, scissors]

player_selection = int(input("Rock(0), paper(1) or scissors(2)? "))
computer_random_number = random.randint(0,2)
computer_choice = game_choices[computer_random_number]
player_choice = game_choices[player_selection]

print(f"Computer chose: {computer_choice}")
print(game_art[computer_random_number])

print(f"You chose: {player_choice}")
print(game_art[player_selection])

if computer_choice == player_choice:
    print("GAME ENDS IN A DRAW!")
elif computer_choice == "paper" and player_choice == "rock":
    print("COMPUTER WINS!")
elif player_choice == "paper" and computer_choice == "rock":
    print("YOU WIN!")
elif computer_choice == "scissors" and player_choice == "paper":
    print("COMPUTER WINS!")
elif player_choice == "scissors" and computer_choice == "paper":
    print("YOU WIN!")
elif computer_choice == "rock" and player_choice == "scissors":
    print("COMPUTER WINS!")
elif player_choice == "rock" and computer_choice =="scissors":
    print("YOU WIN!")

print("\n")
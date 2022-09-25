import random

rock = "rock"
paper = "papper"
scissors = "scissors"

player_move = input("Choose [r]rock, [p]paper, [s]scissors:")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    print("Invalid input. Please try again...")

random_number = random.randint(1, 3)
computer_move = " "

if random_number == 1:
    computer_move = rock
elif random_number == 2:
    computer_move = paper
else:
    computer_move = scissors

if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print("You Win!")
elif computer_move == player_move:
    print("Draw!")
else:
    print("You Lose!")
print("ROCK,PAPER,SCISSORS GAME BY AASTIK")
import random
a = ["rock","paper","scissors"]
comp = random.choice(a)
player =input("please enter your decision here -> ")
print(f"you chose {player} and the computer chose {comp} ")
if comp == "rock" and player == "paper":
  print("computer wins as rock tears the paper")
elif comp == "paper" and player == "rock":
  print("you win as rock tears the paper")
if comp == "paper" and player == "scissors":
  print("you win as scissors cuts the paper")
elif comp == "scissors" and player == "paper":
  print("computer wins as scissors cuts paper")
if comp == "rock" and player == "scissors":
  print("computer wins as rock breaks the scissors")
elif comp == "scissors" and player == "rock":
  print("player wins as rock breaks the scissors")
if comp == player :
  print("both player chose the same option its a tie!")
choice = input("would you like to play again (y/n)?")

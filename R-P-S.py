### Basic beginner Rock Paper Scissors Game, that shows input, print, dictionary use, list, variable, functions and nested ifs

#importing the random py api file
import random

# the function that allows player input and generates a computer random from a given list.
# the choices are stored in a dict list with key bindings to variable choices
def get_choices():
  player_choice = input("Enter a choice(rock, paper, scissors) : ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"Player": player_choice, "Computer": computer_choice}

  return choices

# function to check who wins. It takes player and computer strings as arguments and checks them with a series of if statements
# NOTE no error checking is done here
def check_win(player, computer):
  print (f"Player chose {player} and Computer chose {computer}")
  if player == computer:
    return("Its a tie")
  elif player == "rock":
    if computer == "scissors":
      return ("R>S, You win")
    else:
      return ("P>R You lose")
  elif player == "paper":
    if computer == "rock":
      return ("P>R, You win")
    else:
      return ("S>P You lose")
  elif player == "Scissors":
    if computer == "rock":
      return ("R>S, You lose")
    else:
      return ("S>P You win")
  else:
    return("Its a tie")


#assiging the choices to a variable whereby the DICT can be called by looking up the key binding
r_Choice = get_choices()

#assigning the string return from the check_win function
result = check_win(r_Choice["Player"], r_Choice["Computer"])

#returning the result
print(result)

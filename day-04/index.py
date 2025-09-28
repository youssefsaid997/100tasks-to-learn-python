# We will create a game with python paper , scissors or stone
# the paper 0 stone 1 scissors 2 
# user will choose one of them
# computer will randomize and get a number 
# then some condidtions based on these conditions we will decide which player won!

import random

print('Welcome to the game!')

user_choice = input('Please choose one of 3 - 0 for stone 1, for paper or 2 for scissors!\n')

user_choice_as_int = int(user_choice)
computer_choice = random.randint(0,2)

user_won = (user_choice_as_int == 0 and computer_choice == 2) or (user_choice_as_int == 1 and computer_choice == 0) or (user_choice_as_int == 2 and computer_choice == 1) 

if(user_won ):
    print('You won!!!')
elif(user_choice_as_int == computer_choice):
    print("It is a draw!")
else:
    print('You lost! try again!')

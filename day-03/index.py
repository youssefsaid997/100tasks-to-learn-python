# Python game:

# welcome message -- game
print("Welcome to find the treasure game!")

# take the name of the player
player_name = input('What is your name Captain? ')
# then ask the player first question -- based on the answer message will be displayed
print(f"Okay Captain {player_name} now you should choose direction to go")
direction = input('    Which direction do you choose right -> or <- left ? ')

if(direction == 'left'):
    print("Game Over, You lost!")
else:
    player_status = input('     Okay Captain! Will you swim or wait? ')
    if(player_status == 'swim'):
        print('Game over! you sunk!')
    else:
        door_color = input('Great! You found 3 door red, green or blue? ')
        if(door_color != 'blue'):
            print("You lost this door has fire!")
        else:
            print("Congratulations! You got the treasures!")
# this will behaviour will be repeated 3 times

# based on choices end the game
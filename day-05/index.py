# In this project we will use loops and coditions in Python to create Password-Generator

# first we need to define a list -> a list is like an array in js 

import random

numbers = [0,1,2,3,4,5,6,7,8,9]
sybmols = ['!','@','#','$',"%","&","*"]
letters = ["a","b","c","d","e","f","g","h","i","i","k","m","n","o","p"]

# after defining the list we need to to do something, take info from the user to generate the password
# such as we how long do you want the password and how many numbers do you and how many sybmols
# after that we will use the lists to add value in the list

user_password_length = int(input("How long do you want the password to be? "))
number_of_sybmols= int(input('How many Sybmols do you want to have in your password? '))
user_password= []


for letter in range(12 - number_of_sybmols):
    rand_num_letter = random.randint(0,12)
    if(letter % 2 == 0 ):
        capitaized_letter = str.capitalize(letters[rand_num_letter])
        user_password.append(capitaized_letter)
    else:
        user_password.append(letters[rand_num_letter])
    # print(letter , rand_num)

for sybmol in range(number_of_sybmols):
    rand_num_sybmol = random.randint(0,len(sybmols))
    user_password.append(sybmols[rand_num_sybmol])


password_as_string = ''
random.shuffle(user_password)
print(user_password)

for letter in user_password:
    password_as_string += letter

print(password_as_string)


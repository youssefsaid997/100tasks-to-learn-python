# print('Hello World!')
# my_name = input('What is your name?\n')

# print_my_name = "Hello, " + my_name + "!"
# print(my_name)

# user_age = input('How old are you?\n')

# if(int(user_age ,0) > 0 ):
#     print('Youssef is '+user_age)
# else:
#     print('Please enter Valid Age!')
#     user_age = input("How old are you?\n")

# here we can do something like do while to verify 
# project one of day-1

#Welcome message : Welcome suggest a name for a brand!
# What is your city name
# what is your pet name
# we suggest a brand name of city_name and pet_name

print("Welcome suggest a name for a brand!")

city_name = input('What is your city name?\n')

printed_text_city= "Beautiful city "+ city_name

if(len(city_name)<2):
    print("Please enter a valid city name!")
else:
    print(printed_text_city)

pet_name = input('What is your pet name?\n')

printed_pet_name = "Niceeee!, "+ pet_name

if(len(pet_name)<2):
    print("Please enter a valid city name!")
else:
    print(printed_pet_name)

final_sentence = "Your brand name is " + city_name + " " +pet_name

print(final_sentence)
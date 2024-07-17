import random

on = True

number = random.randint(0,100)

print ("WELCOME TO GUESS THE NUMBER")
print("I thought of a number from 0 to 100")
while on:
    user_input = "Guess the number: "

    if user_input.isdigit():
        guess = int(user_input)
    else:
        print("You have to enter a number!")

    if user_input < number:
        print("Too Low! Guess again!")
    elif user_input > number:
        print("Too High! Guess again!")
    else: 
        print("yay!") 
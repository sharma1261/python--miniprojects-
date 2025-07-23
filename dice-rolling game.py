# dice rolling simulator 


import random  # to generate random dice numbers

print("Welcome to Dice Rolling Simulator!")
choice = "yes"

while choice.lower() == "yes":
    dice_value = random.randint(1, 6)  # generates a random number between 1 and 6
    print("You rolled a:", dice_value)
    
    # Ask user if they want to roll again
    choice = input("Do you want to roll the dice again? (yes/no): ")

print("Thanks for playing!")


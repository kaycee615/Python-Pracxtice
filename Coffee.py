#KCs Coffee Shop Simulator Y2K24
#Copyright 2024 (C) KC Coding, All RIghts Reserved

print("KCs Coffee Shop Simulator Y2K24, version 1.00")
print("Copyright (C) 2024 KC Coding All Rights Reserved.\n")
print("Let's collect some information before we start the game.\n")

# Get player's name and shop name
name = input("What is your name? ")
shop_name = input("What do you want to name your coffee shop? ")

print("\nThanks, " + name + ". Let's set some initial pricing.\n")

# accept input for getting the initial price of a cup of coffee
cup_price = input("What do you want to charge for a cup of coffee? ")

# Display the information collected so far (name, coffee shop name, price per cup)
print("\nGreat! Here's what we have collected so far.\n")
print("Your name is " + name + " and you're opening " + shop_name + "!")
print("Your first cup of coffee will sell for $" + cup_price + ".\n")

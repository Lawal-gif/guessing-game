import random

print("Welcome to the Guessing Game!")
print("I am thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)

guess = 0  # We start with a fake guess so the game can begin

# This 'while' loop keeps running as long as the guess is wrong
while guess != secret_number:
    # Get the player's guess
    guess = int(input("Enter your guess: "))
    
    # Check if the guess is too low, too high, or just right
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the right number!")
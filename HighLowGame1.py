

import random

difficulty = input("Please choose a difficulty level (Easy, Medium, Hard, Legendary): ")

# Setting the lowest and highest values based on the chosen difficulty.
if difficulty.casefold() == "easy":
    lowest_val = 1
    highest_val = 10
    max_guesses = 5
elif difficulty.casefold() == "medium":
    lowest_val = 1
    highest_val = 100
    max_guesses = 10
elif difficulty.casefold() == "hard":
    lowest_val = 1
    highest_val = 500
    max_guesses = 15
elif difficulty.casefold() == "legendary":
    lowest_val = 1
    highest_val = 1000
    max_guesses = 20
else:
    print("Invalid difficulty level. Please try again and type E, M, H, or L.")
    exit()

# Generating a random answer within the specified range.
answer = random.randint(lowest_val, highest_val)
print(answer) # TODO remove this after we finish the code.

guess_count = 0

print("Please enter a number from {} to {}: ".format(lowest_val, highest_val))

# Looping until the correct answer is guessed or the user enters 0 to quit.
while True:
    guess_count += 1

    if guess_count > max_guesses:
        print("You have reached the maximum number of guesses. Game over!")
        break

    guess = int(input())

    if guess == 0:
        break

    elif guess == answer:
        print("Well done! You found the number in", guess_count, "guesses.")
        break

    else:
        if guess < answer:
            print("Please guess higher or type 0 to quit.")
        else:
            print("Please guess lower or type 0 to quit.")
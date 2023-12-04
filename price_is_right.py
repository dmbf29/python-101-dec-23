import random
# randomly select a number (called correct_number)
correct_number = random.randint(1, 100)
# create a variable for the number of user's guesses
guesses = 0
min = 1
max = 100
# START THE LOOP HERE
choice = None
while choice != correct_number:
    # ask the user for a number
    print(f"Choose a number between {min} and {max}")
    # have the player give us a number
    choice = int(input(''))

    # if it's lower than the correct_number, tell them it's lower
    if choice < correct_number:
        min = choice
        print('You need to guess higher!')
    elif choice > correct_number:
        max = choice
        print('You need to guess lower!')
    elif choice == correct_number:
        print('You guessed correctly!')

    guesses = guesses + 1
# END THE LOOP HERE
print(f"It took you {guesses} guesses")
# if it's higher than the correct_number, tell them it's higher
# if it's the same, tell them they guessed correctly
# each time they guess, we want to increment the number of guesses

# when looping, get the game to work one time though THEN link about what needs to be repeated

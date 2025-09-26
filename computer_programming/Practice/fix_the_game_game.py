import random
#def start_game():
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")#You can make this shorter by putting them in the same line of code#no error
number_to_guess = random.randint(1, 100)
max_attempts = 10
attempts = 0
game_over = True
while game_over:#You can make the code shorter by removing the "not"#no error
    guess = int(input("Enter your guess: "))#This was not an integer #run time error
    if attempts >= max_attempts:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
        game_over = False
    elif guess == number_to_guess:#this is supposed to be an elif so that it can't happen in the same thing as the conditional prior#logic error
        print("Congratulations! You've guessed the number!")
        game_over = False
    elif guess > number_to_guess:
        attempts += 1#it needs to move up##logic error
        print("Too high! Try again.")
    elif guess < number_to_guess:
        attempts += 1#it needs to move up#logic error
        print("Too low! Try again.")  
    #continue#continue was redundant#logic error
print("Game Over. Thanks for playing!")
#start_game()#You don't need to contain this in a definition#logic error

##This game is MVP there need to be fewer lines of code. Didnt quite get the local / global scopes and outputting a function to use (dont need easy / high game play) only should need one. Fix it!

from random import *
difficulty = input("Would you like easy or hard difficulty?")
#number_guess = input("Guess a number between 1 - 100")
def play_game():
    if difficulty == "easy":
        play_game_easy()
    elif difficulty == "hard":
        play_game_hard()
def play_game_easy():
    NUMBER=randint(1,100)
    print("You have 10 Guesses!")
    number_guess = int(input("Guess a number between 1 - 100"))
    guesses = 10
    exit_game=False
    while exit_game is False:
        if int(number_guess) != NUMBER and int(number_guess) < NUMBER:
            guesses -= 1
            print(f"The number is higher you have {guesses} left!")
            number_guess = input("Guess a number between 1 - 100")
            if guesses ==1:
                print("you lose!")
                exit_game=True
        elif int(number_guess) != NUMBER and int(number_guess) > NUMBER:
            guesses -= 1
            print(f"The number is lower you have {guesses} left!")
            number_guess = input("Guess a number between 1 - 100")
            if guesses ==1:
                print("you Lose!")
                exit_game=True
        else:
            print("You got it!")
            exit_game=True

def play_game_hard():
    NUMBER=randint(1,100)
    print("You have 5 Guesses!")
    number_guess = int(input("Guess a number between 1 - 100"))
    guesses = 5
    exit_game=False
    while exit_game is False:
        if int(number_guess) != NUMBER and int(number_guess) < NUMBER:
            guesses -= 1
            print(f"The number is higher you have {guesses} left!")
            number_guess = input("Guess a number between 1 - 100")
            if guesses ==1:
                print("you lose!")
                exit_game=True
        elif int(number_guess) != NUMBER and int(number_guess) > NUMBER:
            guesses -= 1
            print(f"The number is lower you have {guesses} left!")
            number_guess = input("Guess a number between 1 - 100")
            if guesses ==1:
                print("you Lose!")
                exit_game=True
        else:
            print("You got it!")
            exit_game=True

play_game()
# def difficulty()
#     print(guess)
    # if guess == "easy":
    #     guesses=10
    # else:
    #     guesses=5
    # return guesses
##Write Function to set a random number as a global variable.

##Ask the user if they want hard or easy
    ##If easy, give 10 guesses
    ##If hard, give 5 guesses
##Compare guessed number to global randInt
    ##If too high (print too high) and take a guess away
    ##If too low, (print too low) and take away a guess
##If guess is the guess, print you got it!

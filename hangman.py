import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
# Global Variables
end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
display = []
lives = 6
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
# find length of chosen word and print "_" for spaces
word_length = len(chosen_word)
for length in range(word_length):
    display.append("_")
print(''.join(display))

# Check on guessed letter
while end_of_game == False:
    guess = input("Guess a Letter. ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(''.join(display))
#Check if guess is in chosen word, if not, subtract a life.(needs to be same indentation as the for loop
    if guess not in chosen_word:
        lives -= 1
        print(f"You have {lives} lives left.")
        print(''.join(display))
        if lives == 0:
            end_of_game = True
            print("End of game.")

    if "_"  not in display:
        end_of_game = True
        print("End of game.")

# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
    print(stages[lives])
print(display)


#rock_paper_scissors.py
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
x = input("What do you chose? Type 0 for Rock, 1 for Paper, or 2 for Scissors?")
list=[rock, paper, scissors]
if x == "0":
    print(rock)
elif x == "1":
    print(paper)
elif x == "2":
    print(scissors)    
else:
    print("invalid entry, Type 0 for Rock, 1 for Paper, or 2 for Scissors" )
print("The computer chose:")
computer_choice = random.choice(list)
print(computer_choice)

if x == "0" and computer_choice == rock:
    print("Draw")
elif x == "0" and computer_choice == paper:
    print("You lose!")
elif x == "0" and computer_choice == scissors:
    print("You win!!")
elif x == "1" and computer_choice == rock:
    print("You win!!")
elif x == "1" and computer_choice == paper:
    print("Draw!")
elif x == "1" and computer_choice == scissors:
    print("You lose!!")
elif x == "2" and computer_choice == rock:
    print("You lose :( !!")
elif x == "2" and computer_choice == paper:
    print("You win :) !")
elif x == "2" and computer_choice == scissors:
    print("Draw")
else:
    print("something went wrong")

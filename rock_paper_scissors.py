#rock_paper_scissors.py

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
import random

x = print(input("What do you chose? Type 0 for Rock, 1 for Paper, or 2 for Scissors?"))
list=[rock, paper, scissors]
print(list[])
computer_choice = random.choice(list)
print(computer_choice)

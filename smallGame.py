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
# rock paper scissors with computer
game_choices = [rock,paper,scissors]
# user_input or choice
user_choice = int(input("choose one 0.rock 1.paper, 2.scissors: "))
if user_choice >=3 or user_choice < 0:
  print("Invalid input.")
else:
  if user_choice == 0:
    print("you choosed 0: rock",game_choices[user_choice])
  elif user_choice == 1:
    print("you choosed 1: paper",game_choices[user_choice])
  else:
    print("you choosed 2: scissors",game_choices[user_choice])
  
  #computer choice or input
  computer_choice = random.randint(0,2) 
  if computer_choice == 0:
    print("computer choosed 0: rock",game_choices[computer_choice])
  elif computer_choice == 1:
    print("computer choosed 1: paper",game_choices[computer_choice])
  else:
    print("computer choosed 2: scissors",game_choices[computer_choice])

  # win or lose

  if user_choice == computer_choice:
    print("It's draw.")
  elif (user_choice - computer_choice) == -1:
    print("You lose!")
  elif user_choice < computer_choice:
    print("You win :)")
  elif (computer_choice - user_choice) == -1:
    print("You win :)")
  elif computer_choice < user_choice:
    print("You lose!")
  else:
    print("Get the hell out of here,System crashed")


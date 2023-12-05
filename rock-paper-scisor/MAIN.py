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

import random
game_rules = {"rock": ["scissors"],"scissors": ["paper"],"paper": ["rock"]}
user_choice = input("Chose rock, paper or scissor.").lower()
computer_choice = random.choice(list(game_rules.keys()))

print(f"You chose {user_choice}.")
print(eval(user_choice))
print("Computer choses:",computer_choice)
print(eval(computer_choice))

if user_choice == computer_choice:
  print("It´s a draw.")
elif computer_choice in game_rules[user_choice]:
  print("Congratulations, you WIN!")
else:
  print("Better luck next time, you lose!")
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
shapes=[rock,paper,scissors]
print("Welcome to Rock, Paper, Scissors!")
user_choice = int(input("Enter 0 for Rock, 1 for Paper, or 2 for Scissors: "))
if user_choice < 0 or user_choice > 2:
    print("Invalid choice. Please enter 0, 1, or 2.")
else:
    print(f"you chose:\n{shapes[user_choice]}")
    computer_choice=random.randint(0,2)
    print(f"computer chose:\n{shapes[computer_choice]}")
    if user_choice==computer_choice:
        print("its a draw")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("you win")
    else:
        print("you lose")

import random
Rock = '''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
Scissor = '''
      _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [Rock, Paper, Scissor]
choice = int(input("What do u choose? Type 0 for rock,1 for Paper, 2 for Scissor\n"))
print(game_images[choice])
computer_choice = random.randint(0, 2)
print(f"Computer choose {computer_choice}")
if choice >= 3 or choice < 0:
    print("You typed an invalid number, you lose!")
elif choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and choice == 2:
    print("You lose")
elif computer_choice > choice:
    print("You lose")
elif choice > computer_choice:
    print("You win!")
elif choice == computer_choice:
    print("Draw!")

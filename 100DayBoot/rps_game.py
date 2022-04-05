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
game_images = [rock, paper, scissors]

player_choice = (int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")))

if player_choice >= 3 or player_choice < 0:
  print("You have typed an invalid number, you lose!")
else:
  print(game_images[player_choice])


  comp_choice = random.randint(0,2)
  print("computer chose:")
  print(game_images[comp_choice])

  if player_choice == 0 and comp_choice == 2:
    print("You Win!")
  elif player_choice == 1 and comp_choice == 0:
    print("You Win!")
  elif comp_choice == 0 and player_choice == 2:
    print("You Lose!")
  elif comp_choice > player_choice:
    print("You Lose!")
  elif player_choice > comp_choice:
    print("You Win!")

  elif comp_choice == player_choice:
      print("It's a Draw!")




# print(player_choice)
# print(comp_choice)

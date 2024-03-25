import random
rock = ''''
    (______)
    (______)
'''
paper = ''''
  _________)
  _________)
  _________)
'''
scissors = '''
   ____________)
   __________)
   _____________)
   __________)
'''
game_images = [rock,paper,scissors]
users_choice = int(input("enter your choice type 0 for rock , 1 for paper ,2 for scissors :"))
if users_choice >= 3 or users_choice < 0:
    print("you entered invalid number, you lose")
else:
    print("users_choice:")
    print(game_images[users_choice])
    computer_choice = random.randint(0,2)
    print("computer_choice:")
    print(game_images[computer_choice])
    print(computer_choice)
    if computer_choice == users_choice:
        print("Draw match")
    elif computer_choice < users_choice:
        print("you lose")
    elif computer_choice > users_choice:
        print("you win")
    elif computer_choice == 0 and users_choice == 2:
        print("you lose")
    elif computer_choice == 2 and users_choice == 0:
        print("you lose")
    elif computer_choice >= 3 or users_choice < 0:
        print("you entered invalid number, you lose")

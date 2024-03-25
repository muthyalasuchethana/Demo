import random
number = random.randint(1,101)
guess = 0
while guess!=number:
    guess = int(input("guess a number between 1 to 101 : "))

    if guess<number:
        print("guess higher")
    elif guess>number:
        print("guess lower")
    else:
        print("you won!!")

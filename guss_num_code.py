# Method 1
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

# method 2
import random
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5
def set_difficulty(level_chosen):
    if level_chosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
def check_answer(guessed_number, answer, attempts):
    if guessed_number<answer:
        print("your guess is too low")
        return attempts - 1
    elif guessed_number>answer:
        print("your guess to too high")
        return attempts - 1
    else:
        print(f"your guess is right! and the answer was {answer}")

def game():
    print("let me think  a number between 1 to 50")
answer = random.randint(0, 51)
level = input("choose level of difficulty 'easy' or 'difficult' ")
attempts = set_difficulty(level)
guessed_number = 0
while guessed_number != answer:
    print(f"you have {attempts} to guess the number")
    guessed_number = int(input("guess a number : "))
    attempts = check_answer(guessed_number, answer, attempts)
    if attempts == 0:
        print("your out of guesses....you lose!")
        break
    else:
        print("guess again")

game()

import random
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["@", "#", "%", "!", "|", "/"]
print(" Welcome to password generators ")
n_alphabets = int(input("how many alphabets you want : "))
n_numbers = int(input("how many numbers you want : "))
n_symbols = int(input("how may symbols you want : "))
password = ""
for i in range(n_alphabets+1):
    char = random.choice(alphabets)
    password += char
for i in range(n_numbers + 1):
    num = random.choice(numbers)
    password += num
for i in range(n_symbols + 1):
    sym = random.choice(symbols)
    password += sym
print(password)

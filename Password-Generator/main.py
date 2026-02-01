import random 
import string

password = []

list_of_digits = list(string.digits)
list_of_symbols = list(string.punctuation)
list_of_letters = list(string.ascii_letters)

no_of_letters = int(input("How many letters you want? "))
no_of_digits = int(input("How many digits you want? "))
no_of_symbols = int(input("How many symbols you want? "))

def digits():
    return random.choice(list_of_digits)
def letters():
    return random.choice(list_of_letters)
def symbs():
    return random.choice(list_of_symbols)


for i in range(no_of_digits):
    numbers = digits()
    password.append(numbers)
for i in range(no_of_letters):
    characters = letters()
    password.append(characters)
for i in range(no_of_symbols):
    special_symbs = symbs()
    password.append(special_symbs)

print(password)


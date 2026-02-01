import random 
import string

list_of_digits = list(string.digits)
list_of_symbols = list(string.punctuation)
list_of_letters = list(string.ascii_letters)

no_of_letters = int(input("How many letters you want? "))
no_of_digits = int(input("How many digits you want? "))
no_of_symbols = int(input("How many symbols you want? "))

def digits():
    numbers = random.choice(list_of_digits)
    return numbers
def letters():
    characters = random.choice(list_of_letters)
    return characters
def symbs():
    special_symbs = random.choice(list_of_symbols)
    return symbs

for i in range(no_of_digits):
    digits()
for i in range(no_of_letters):
    letters()
for i in range(no_of_symbols):
    symbs()


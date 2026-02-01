'''
import strings
digits = list(string.digits)
symbols = list(string.punctuation)
'''

import random 

list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
 'U', 'V', 'W', 'X', 'Y', 'Z']

list_of_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list_of_symbols = ['!', '#', '$', '%', '&','*', '-', '.' '@']

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


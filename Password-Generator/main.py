'''
import strings
digits = list(string.digits)
symbols = list(string.punctuation)
'''

import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
 'U', 'V', 'W', 'X', 'Y', 'Z']

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
 '+', ',', '-', '.', '/', ':', ';', '<', '=', '>',
 '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
 '}', '~']

no_of_letters = int(input("How many letters you want? "))
no_of_digits = int(input("How many digits you want? "))
no_of_symbols = int(input("How many symbols you want? "))

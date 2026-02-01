print('''\nWelcome to the Password Generator!\n
We ensure to generate the Strong Passwords.\n\n''')

import random 
import string

list_of_digits = list(string.digits)
list_of_symbols = list(string.punctuation)
list_of_letters = list(string.ascii_letters)

while True :

    password = []

    try:
        no_of_letters = int(input("How many letters you want?\n "))
        no_of_digits = int(input("How many digits you want?\n "))
        no_of_symbols = int(input("How many symbols you want?\n "))
     
        
        if no_of_letters == 0 or no_of_digits == 0 or no_of_symbols == 0:
            print('''          Warning! 
                Make sure your password contain letters,digits & symbols
                So that attackers fail to crack...''')
        else :
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

            random.shuffle(password)

            for i in password:
                print(i , end = '')
            
            break

    except ValueError:
        print("Please enter a valid number of times.")
    
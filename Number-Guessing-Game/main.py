import random

number_to_guess = random.randint(1,100)

while True:
    try :
        user_guess = int(input("Guess the number between 1 and 100: "))
        
        if user_guess >= 1 and user_guess <= 100:
            if user_guess < number_to_guess :
                print("Too low!")
            elif user_guess > number_to_guess :
                print("Too high!")
            elif user_guess == number_to_guess :
                print("Congratulations! You guessed the number.")
                break
        else :
            print("Please enter a value in the range 1 to 100!")    
    except ValueError :
        print("Please enter a valid number")

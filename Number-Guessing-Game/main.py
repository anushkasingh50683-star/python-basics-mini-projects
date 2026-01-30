import random

number_to_guess = random.randint(1,100)

def user_play_again():
    number_guessing_game()
     
def number_guessing_game():
    if user_guess >= 1 and user_guess <= 100:
            if user_guess < number_to_guess :
                print("Too low!")
            elif user_guess > number_to_guess :
                print("Too high!")
            elif user_guess == number_to_guess :
                print("Congratulations! You guessed the number.")
                play_again = input("Do you want to play again? (y/n): ").lower()
                while True:
                    try :
                        if play_again == 'y':
                            user_play_again()
                        elif play_again == 'n':
                            print("Thank You for playing!")
                            break
                        else:
                            print("Enter a valid choice (y/n)")
                            continue
                    except ValueError :
                        print("Enter a valid choice (y/n)")
    else :
        print("Please enter a value in the range 1 to 100!") 

while True:
    try :
        user_guess = int(input("Guess the number between 1 and 100: "))
        number_guessing_game()  
    except ValueError :
        print("Please enter a valid number")




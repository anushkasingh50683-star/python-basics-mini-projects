import random
print("Welcome to the Rock-Paper-Scissors Game")
print("Let's start..")

all_moves = ['Rock','Paper','Scissors']

while True:
    computer_move = random.choice(all_moves)
    print(computer_move)
    user_guess = input("Enter your move (rock/paper/scissors): ").lower()

    if computer_move == 'Rock' and user_guess == 'rock':
        print("Tie")
    elif computer_move == 'Rock' and user_guess == 'paper':
        print("You Won!")
    elif computer_move == 'Rock' and user_guess == 'scissors':
        print("You Lose!")
    elif computer_move == 'Paper' and user_guess == 'rock':
        print("You lose!")
    elif computer_move == 'Paper' and user_guess == 'paper':
        print("Tie")
    elif computer_move == 'Paper' and user_guess == 'scissors':
        print("You won!")
    elif computer_move == 'Scissors' and user_guess == 'rock':
        print("You won!")
    elif computer_move == 'Scissors' and user_guess == 'paper':
        print("You Lose!")
    elif computer_move == 'Scissors' and user_guess == 'scissors':
        print("Tie")


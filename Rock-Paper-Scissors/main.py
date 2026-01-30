import random
print("Welcome to the Rock-Paper-Scissors Game")
print("Let's start..")
print("The scores you can play for:-")
print("Low: 5")
print("Med: 10")
print("High: 20")
global user_wins
global computer_wins
user_wins = 0
computer_wins = 0
def game():
    global user_wins
    global computer_wins
    all_moves = ['Rock','Paper','Scissors']
    computer_move = random.choice(all_moves)
    user_move = input("Enter your move (rock/paper/scissors): ").lower()

    if computer_move == 'Rock' and user_move == 'rock':
        print(f"Your move {user_move}. Computer Move {computer_move}.")
        print("Tie")
    elif computer_move == 'Rock' and user_move == 'paper':
        print(f"Your move {user_move}. Computer Move {computer_move}.")
        print("You Won!")
        user_wins += 1
    elif computer_move == 'Rock' and user_move == 'scissors':
        print(f"Your move {user_move}. Computer Move {computer_move}.")
        print("You Lose!")
        computer_wins += 1
    elif computer_move == 'Paper' and user_move == 'rock':
        print(f"Your move {user_move}. Computer Move {computer_move}.")
        print("You lose!")
        computer_wins += 1
    elif computer_move == 'Paper' and user_move == 'paper':
        print(f"Your move {user_move}. Computer Move {computer_move}.")
        print("Tie")
    elif computer_move == 'Paper' and user_move == 'scissors':
        print(f"Your move {user_move}. Computer Move {computer_move}.")
        print("You won!")
        user_wins += 1
    elif computer_move == 'Scissors' and user_move == 'rock':
        print(f"Your move {user_move}. Computer Move {computer_move}.")
        print("You won!")
        user_wins += 1
    elif computer_move == 'Scissors' and user_move == 'paper':
        print(f"Your move {user_move}. Computer Move {computer_move}.")
        print("You Lose!")
        computer_wins += 1
    elif computer_move == 'Scissors' and user_move == 'scissors':
        print(f"Your move {user_move}. Computer Move {computer_move}.")
        print("Tie")
    else:
        print("Please select a valid choice - rock/paper/scissors")
scores = int(input("For how many scores you wanna compete with Mr Computer Ji? "))
if scores == 5:
    for i in range(5):
        game()
elif scores == 10:
    for i in range(10):
        game()
elif scores == 20:
    for i in range(20):
        game()
print("Well played..")

if computer_wins > user_wins:
    print("But You lost!")
elif computer_wins < user_wins:
    print("Congratulations! You Won.")
elif computer_wins == user_wins:
    print("Tie!")

import random

rounds_played = 0
total_dice_rolled = 0

while True:
    user = input("Roll the dice? (y/n):").lower()
    if user == 'y':
        try:
            n = int(input("How many dice you want to roll? ")) 
            if n == 0:   
                print("No dice rolled.")
            elif n < 0:   
                print("No. of dice to roll can't be negative!")
            else:
                result = []
                for i in range(n):
                    die= random.randint(1,6)
                    result.append(die)
                print(tuple(result))
                rounds_played += 1
                total_dice_rolled += n
        except ValueError:
            print("Please enter a valid integer.")
    elif user == 'n':
        print("Number of times you rolled the dice =",rounds_played)
        print("Total dice rolled:", total_dice_rolled)
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")


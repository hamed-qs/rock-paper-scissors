import random


def game():
    list = ["rock", "paper", "scissors"]
    pc = random.choice(list)
    print("-------------------------------")
    print("ROCK, PAPER, SCISSORS\n")
    you = input("Get 'r' for Rock, 'p' for Paper, 's' for Scissors: ")
    while you.isalpha() == False:
        you = input("\n\nPlease enter 'r' for Rock, 'p' for Paper, 's' for Scissors: ")
    while you != 'r' and you != 'p' and you != 's':
        you = input("\n\nPlease enter 'r' for Rock, 'p' for Paper or 's' for Scissors: ")

    if pc == "rock" and you == "s":
        print(f"\nYou scissors and pc {pc}. Pc won\n")
    elif pc == "paper" and you == "r":
        print(f"\nYou rock and pc {pc}. Pc won\n")
    elif pc == "scissors" and you == "p":
        print(f"\nYou paper and pc {pc}. Pc won\n")

    
    elif pc == "rock" and you == "p":
        print(f"\nYou paper and pc {pc}. You won\n")
    elif pc == "paper" and you == "s":
        print(f"\nYou scissors and pc {pc}. You won\n")
    elif pc == "scissors" and you == "r":
        print(f"\nYou rock and pc {pc}. You won\n")
    else :
        print(f"\nYou {pc} and pc {pc}, Draw\n")
    
game()

command = input("\nWould you like to play again, 'y' or 'n': ")
print("\n")
if command == "y":
    game()
    second_command = input("\nWould you like to play again, 'y' or 'n': ")
    print("\n")
    while second_command == "y":
        game()
        second_command = input("\nWould you like to play again, 'y' or 'n': ")
        print("\n")
        if second_command != "y":
            print("Thanks for playing")


else:
    print("Thanks for playing")
        

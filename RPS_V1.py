# Rock, Paper, Scissors Game
# --------------------------
# This program allows a user to play Rock, Paper, Scissors against the computer.
# The user inputs their choice, the computer randomly selects one,
# and the program determines the winner.
# The game continues until the user chooses to quit.

import random 

choices = ['r','p','s']
emojis = {'r':'🪨','p':'📄','s':'✂️'}

def verify_input():
    while True:
        user_guess=input("Rock, paper or scissors? (r/p/s):").lower()
        if user_guess in choices:
            return user_guess
        else:
            print("Invalid Argument")


def display_choises(user, computer):
    print( f'You chose {emojis[user]}')
    print( f'Computer chose {emojis[computer]}') 


def find_winner(user, computer):
    if user == computer:
        print("Match is a draw")

    elif(
        (user == 'r' and computer == 's') or
        (user == 'p' and computer == 'r') or
        (user == 's' and computer == 'p')
    ):
        print('You win')
    else:
        print('You lose')

def play_game():
    while True:
        user = verify_input()

        computer = random.choice(choices)

        display_choises(user, computer)

        find_winner(user,computer)

        need_continue = input('Continue? (y/n): ').lower()
        if need_continue == 'n':
            break

play_game()


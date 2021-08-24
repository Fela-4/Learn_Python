import random


# This is a test script
import math
from pprint import pprint

if __name__ == "__main__":
    print(math.pi)
    print("Running script...")
    a = 10
    b = 5
    res = 10 / 5
    print(res)
    u_duct = {
        "one": 1,
        "two": 2,
        "three": 3,
    }
    pprint(u_duct)

#Rock Paper Scissors Game

def is_win(user, computer)
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


def play()
    user= input("What is your choice: 'p' for paper, 'r' for rock and 's' for scissors\n")
    comp = random.choice(['r','p','s']) 

    if user == computer:
        return "It's a tie"
    if is_win(user, computer)
        return "You won!"
    return "You lost!"


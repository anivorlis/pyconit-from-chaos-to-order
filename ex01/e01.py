# We will implement a function that rolls a dice [1-6]
# We will use the standard library and numpy for that! 

import random

def roll_dice() -> int:
    return random.randint(1, 6)


if __name__ == '__main__':
    print(roll_dice())


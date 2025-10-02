import random

class ValueTooHighError(Exception):
    pass


try:
    random_number = random.randint(1, 100)

    number = int(input("Guess a number: "))

    if number > 100:
        raise ValueTooHighError

    if number == random_number:
        print("YOU WON!")
    elif number != random_number:
        print("YOU LOST!")
        print(f"The correct number is: {random_number}")
except ValueTooHighError:
    print("Error: Maintain the range 1-100")
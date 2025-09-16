introduction = (''' 
Let's Play a Game!
Guess the number to win a prize!
Remember you only have two guesses
------------LET"S GO!!--------------  
                    ''')
print(introduction)

correct_guess = 6
guess_limit = 3
guess_count = 0

while guess_count < guess_limit:
    guess_count +=1
    players_guess = input("Guess: ")
    if int(players_guess) == correct_guess:
        print("You Won!.")
        break
    elif int(players_guess) != correct_guess:
        print("You have FAILED!")
    else:
        print("ERROR: Please guess a number.")
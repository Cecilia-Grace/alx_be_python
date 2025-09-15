instructions = """
            Instructions.
            TO START, PRESS ANY KEY THEN ENTER
            FOLLOW WITH THE BELOW TO PLAY THE GAME!

             start - to start the car
             stop - to stop the car
             quit - to quit and exit the game
             """
print(instructions)

action = input("> ")

while action.lower():
    action = input("> ")
    if action.lower() == "start":
        print("Car has started ...Let's Go!")
    elif action.lower() == "stop":
        print("Car has stopped ...")
    elif action.lower() == "quit":
        print("Game ended. See you soon!")
        break
    else:
        print("Please read the instructions above.")

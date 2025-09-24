for number in range(1, 101):
    number = input("Enter a number or q to quit: ")
    if number.lower() == "q":
        break

    if int(number) % 5 == 0 and int(number) % 3 == 0:
        print(f"{number} is divisible by both 3 and 5.")
    elif int(number) % 3 == 0:
        print(f"{number} is divisible by 3.")
    elif int(number) % 5 == 0:
        print(f"{number} is divisible by 5.")
    elif int(number) % 2 == 0:
        print(f"{number} is divisible by 2")
    else:
        print(f"{number} is not divisible by either 3 or 5.")
    

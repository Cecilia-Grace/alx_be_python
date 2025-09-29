def names_arranged_alphabetically():
    names = []

    while True:

        print("""
                Instruction.
              Type 1 to add another name.
              Type 2 to arrange the names added.
              Type 0 to quit.
             """)
        instruction_number = input("Enter a number: ")

        if instruction_number == "1":
            user_name = input("Enter a name: ")
            names.append(user_name)
            print(names)
        elif instruction_number == "2":
            names.sort()
            print(names)
        elif instruction_number == "0":
            print("Goodbye")
            break
        else:
            print("Please enter correct input.")
        

names_arranged_alphabetically()
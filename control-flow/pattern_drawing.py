while True:
    size_input = input("Enter the size of the pattern: ")
    if size_input.isdigit() and int(size_input) > 0:
        size = int(size_input)
        break
    else:
        print("Invalid input. Please enter a positive integer.")

row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    
    print()  
    
    row += 1
        
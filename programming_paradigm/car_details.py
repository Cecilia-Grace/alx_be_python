class Car:
    def __init__(self, color, car_type):
        self.color = color
        self.car_type = car_type
        
    def car_details(self):
        print(f"This is a {self.color} {self.car_type}.\n")
    

car_type_list = []

while True:
    color = input("What color is the car: ")                 
    car_type = input("What type is the car: ")   
    car = Car(color, car_type)
    car.car_details()
    
    car_type_list.append(car_type)
    
    quit = input("Do you want to quit (yes/no)? ").lower()
    
    if quit == "yes":
        print(f"You have the following cars: {car_type_list}")
        print("Goodbye")
        break
    elif quit == "no":
        continue
        
        




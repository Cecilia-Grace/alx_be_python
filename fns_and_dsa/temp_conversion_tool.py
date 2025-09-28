FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = int(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

def convert_to_celsius(temperature):
    celsuis = (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return f"{temperature}°F is {celsuis}°C"


def convert_to_fahrenheit(temperature):        
    fahrenheit = (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return f"{temperature}°C is {fahrenheit}°F"


if unit == "f":
    print(convert_to_celsius(temperature))
elif unit == "c":
    print(convert_to_fahrenheit(temperature))
else:
    print("Invalid temperature. Please enter a numeric value.")


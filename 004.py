"""Problem 004: Convert temperature from Celsius to Fahrenheit and vice versa"""

choice = input("Convert from (C)elsius or (F)ahrenheit? ").strip().lower()
temperature = float(input("Enter temperature: "))
if choice == "c":
    print("Fahrenheit:", temperature * 9 / 5 + 32)
elif choice == "f":
    print("Celsius:", (temperature - 32) * 5 / 9)
else:
    print("Please enter C or F.")

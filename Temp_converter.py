num = float(input("Enter the number of temperature "))
unit = input ("Enter the unit (C for celsius) ,(K for kelvin) and (F for fernaheit) : ")
if unit.upper() == "C":
    kelvin = num + 273.15
    fernaheit = (num * 9/5) + 32
    print(f"{num} degree celsius is equal to {round(kelvin,2)} kelvin and {round(fernaheit,2)} fernaheit")
elif unit.upper() == "K":
    celsius = num - 273.15
    fernaheit = (num - 273.15) * 9/5 + 32
    print(f"{num} kelvin is equal to {round(celsius,2)} celsius and {round(fernaheit,2)} fernaheit")
elif unit.upper() == "F":
    celsius = (num - 32) * 5/9
    kelvin = (num - 32) * 5/9 + 273.15
    print(f"{num} fernaheit is equal to {round(celsius,2)} celsius and {round(kelvin,2)} kelvin")
else:
    print("Invalid unit. Please enter C, K, or F.")
def convert_temperature(temp, unit):
    if unit == 'C':
        return (temp * 9/5) + 32
    else:
        return (temp - 32) * 5/9

temp = float(input("Enter temperature: ")) 
unit = input("Enter 'C' for Celsius, 'F' for Fahrenheit: ").upper()

if unit not in ['C', 'F']:
    print("Invalid unit! Enter C or F.")
else:
    print("Converted Temperature:", convert_temperature(temp, unit))

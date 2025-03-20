year = int(input("Enter a year: "))

if year < 0:
    print("Year cannot be negative!")
elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

bill=float(input("Enter the bill amount: "))
tip=int(input("Enter the tip percentage: "))
if bill < 0 or tip < 0:
    print("bill and tip cant be negative")
else:
    tip=(tip/100*bill)
    totalbill= bill+tip
    print("the tip amount is:", tip)
    print("the total bill amount is :", totalbill)


            
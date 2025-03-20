speed=int(input("enter the speed:"))
limit=60
if speed < 0:
    print("speed cant be negative")
elif speed > limit:
    fine=(speed-limit)*10
    print("over speeding!!, fine is", fine)
else:
    print("No fine,drive safe!!")
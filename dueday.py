due_day=int(input("enter the due days:"))
if due_day < 0:
    print("due day cant be negative:")
    fine=0
elif due_day <= 5:
    fine=due_day*2
elif due_day <= 10:
    fine=due_day*5
else:
    fine=due_day*10


print("fine is:", fine)
balance=5000
choice=input("enter 'D' for deposit, 'W' for withdrawal").upper()
if choice not in ['D','W']:
    print("Invaild choice: enter D or W")
else:
    amount=float(input("enter the amount:"))
    if amount < 0:
        print("amountcant be in negative")
    elif choice == 'D':
        balance += amount
    elif choice == 'W' and amount >balance:
        print("insufficient balance")
    else: balance -= amount

print("updated balance:", balance)

balance=5000
withdraw=int(input("Enter the amount to withdraw: "))
if withdraw < 0:
    print("withdrawal amount is negative number enter")
elif withdraw > balance:
    print("insfficient balance")
else:
    balance -= withdraw 
    print("withdrawal successful, remaining balance is",balance)
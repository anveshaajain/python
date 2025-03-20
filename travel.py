distance=int(input("Enter the distance travelled in km:"))
fare=0
if distance <0:
    print("distance cant be negative")
elif distance <=5:
    fare=10
elif distance <= 15:
    fare=25
else:
    fare=40

print("total fare is:", fare)

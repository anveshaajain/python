sentence=input("enter the sentence:")
vowles="aeiouAEIOU"
count=0
for char in sentence:
    if char in vowles:
       count+=1


print("vowles in the sentence are:" , count) 
password=input("enter the password:")
if len(password) < 8:
    print("password is weak: too short!!")
elif password.isalpha() or password.isdigit():
  print("pasword is weak: use mix characters")
else:
   print("password is strong")

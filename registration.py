registered_emails = set()
email = input("Enter your email: ")
if email in registered_emails:
    print("Email already registered.")
else:
    registered_emails.add(email)
    print("Registration successful.")

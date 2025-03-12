def is_palindrome(number):
    return str(number) == str(number)[::-1]

def main():
    num = int(input("Enter a number: "))
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")

main()

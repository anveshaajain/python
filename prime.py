def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num1, num2 = map(int, input("Enter two numbers: ").split())

if is_prime(num1):
    print(f"{num1} is Prime")
else:
    print(f"{num1} is Not Prime")

if is_prime(num2):
    print(f"{num2} is Prime")
else:
    print(f"{num2} is Not Prime")
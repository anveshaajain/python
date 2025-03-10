def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    while a < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def main():
    number = int(input("Enter a number: "))
    fib_list = fibonacci(number)
    print(f"Fibonacci sequence up to {number}: {fib_list}")

if __name__ == "__main__":
    main()
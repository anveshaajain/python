def square(x):
    return x ** 2

print(square(5))

def add(a, b):
    return a + b

print(add(3, 4))

# Using list comprehension to square numbers
numbers = [1, 2, 3, 4]
squared = [x ** 2 for x in numbers]
print(squared)
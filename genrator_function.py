def square_numbers(nums):
    for i in range(nums):
        yield i * i
        
gen = square_numbers(3)
print(list(gen))
def reverse_string(string):
    reversed_str = string[::-1]
    return reversed_str

def main():
    user_input = input("Enter a string: ")
    reversed_result = reverse_string(user_input)
    print("Original string:", user_input)
    print("Reversed string:", reversed_result)

main()


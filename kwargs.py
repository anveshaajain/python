def print_info(**info):
    for key, value in info.items() :
        print(f"{key}:{value}")
    
print_info(name="Alice", age=25, city="NYC")
print_info(name="Bob", age=30, city="Boston")
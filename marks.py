def grade(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    else:
        return 'F'

marks = []  

for i in range(3):
    mark = int(input(f"Enter the mark for subject {i+1} (0-100): "))  
    if 0 <= mark <= 100:
        marks.append(mark)
    else:
        print("Marks should be between 0 - 100.")

print("Grade is:", grade(marks))  

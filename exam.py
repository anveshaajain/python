def attendance(total, attended):
    if total < 0 or attended < 0 or attended > total:
        return "Invalid input!! Attendance must be between 0 and total classes."
    
    percentage = (attended / total) * 100
    return f"Attendance: {percentage:.2f}% - " + ("Allowed for exam" if percentage >= 75 else "Not allowed for exam")

total_classes = int(input("Enter total classes: "))
attended_classes = int(input("Enter attended classes: "))

print(attendance(total_classes, attended_classes))

# Task 1: Student Marks Lookup

# Step 1: Create dictionary of students and marks
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90,
    "Ethan": 88
}

# Step 2: Ask the user to enter a student's name
student_name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve marks or display not found message
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")

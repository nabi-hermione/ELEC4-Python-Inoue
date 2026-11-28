# Full Name: Kate Diane Inoue
# Section: IV-BSIT B
# Activity: Set 1 - P3 Student Record Manager
# Date: November 28, 2026

# stores student names
students = []

# checks for duplicate names
student_set = set()

# add a student
def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    # makes name checking case-insensitive
    name_key = name.casefold()

    if name_key in student_set:
        print("Student already exists.")
    else:
        students.append(name)
        student_set.add(name_key)
        print(f"{name} has been added successfully.")
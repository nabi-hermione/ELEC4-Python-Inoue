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

# remove a student
def remove_student():
    name = input("Enter student name to remove: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    # checks the name without case differences
    name_key = name.casefold()

    if name_key in student_set:
        for student in students:
            if student.casefold() == name_key:
                students.remove(student)
                break

        student_set.remove(name_key)
        print(f"{name} has been removed successfully.")
    else:
        print("Student not found.")

# search for a student
def search_student():
    search_name = input("Enter student name to search: ").strip()

    if not search_name:
        print("Please enter a name to search.")
        return

    # allows partial and case-insensitive searching
    search_key = search_name.casefold()

    matches = [
        student for student in students
        if search_key in student.casefold()
    ]

    if matches:
        print("\n===== SEARCH RESULTS =====")

        for student in matches:
            print(student)

        print(f"Total matches: {len(matches)}")
    else:
        print("No matching student found.")

# display all students
def display_students():
    if not students:
        print("No students registered yet.")
        return

    # sorts student names alphabetically
    sorted_students = sorted(students, key=str.casefold)

    print("\n===== STUDENT LIST =====")

    for number, student in enumerate(sorted_students, start=1):
        print(f"{number}. {student}")

    # displays the total number of students
    print(f"\nTotal students: {len(students)}")

# display menu and handle user choices
def main():
    while True:
        print("\n===== STUDENT RECORD MANAGER =====")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Thank you for using Student Record Manager!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

# run the main function
if __name__ == "__main__":
    main()

# Ang list ay ginagamit para mag-store ng maraming student names and to maintain ang pagkaka-ayos
# kung paano sila nilagay sa program, example is yung students na list kung saan
# naka-store lahat ng name ng students na ina-add ng user.
# Kapag set naman ay ginagamit ito para mag-store ng unique values, meaning hindi dapat
# magkaroon ng duplicate entries example is yung student_set ang ginamit para
# malaman kung existing na ba yung name na gustong idagdag ng user.
# In summary, ang list ay ginagamit para i-store at i-display ang student names,
# habang ang set naman ay ginagamit para maiwasan ang duplicate names sa program.
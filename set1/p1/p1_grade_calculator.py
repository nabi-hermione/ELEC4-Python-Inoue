# Full Name: Kate Diane Inoue
# Section: IV-BSIT B
# Activity: Set 1 - P1: Student Grade Calculator
# Date: November 22, 2026

SUBJECTS = [
    "LN01_CAP 102 - Capstone Project 2",
    "LNO1_ELEC3 - Elective 3 (Special Topics on Web and Mobile 1)",
    "LNO1_ELEC4 - Elective 4 (Special Topics on Web and Mobile 2)",
    "LNO1_IAS 102 - Information Assurance and Security 2",
    "LNO1_SA 101 - System Administration and Maintenance",
    "LNO1_SIA 101 - System Integration and Architecture"
]

# accept and validate student grades
def get_grades():
    grades = {}

    # ask for a grade for each subject
    print("===== ENTER YOUR GRADE FOR EACH SUBJECT =====")

    for subject in SUBJECTS:
        while True:
            try:
                grade = float(input(f"{subject}: "))

                if 0 <= grade <= 100:
                    grades[subject] = grade
                    break
                else:
                    print("Invalid grade. Enter a grade from 0 to 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    return grades

# compute the average grade
def compute_average(grades):
    if not grades:
        return 0

    return sum(grades.values()) / len(grades)

# get the highest grade
def highest_grade(grades):
    if not grades:
        return 0

    return max(grades.values())

# get the lowest grade
def lowest_grade(grades):
    if not grades:
        return 0

    return min(grades.values())

# pass or fail status
PASSING_GRADE = 75

def pass_fail_status(grades):
    average = compute_average(grades)

    if average >= PASSING_GRADE:
        return "PASSED"
    else:
        return "FAILED"

# display all student grade results
def display_results(grades):
    if not grades:
        print("No grades available. Please enter grades first.")
        return

    average = compute_average(grades)
    status = pass_fail_status(grades)

    print("\n===== STUDENT GRADE RESULTS =====")

    print(f"Your average grade is: {average:.2f}")
    print(f"Your highest grade is: {highest_grade(grades):.2f}")
    print(f"Your lowest grade is: {lowest_grade(grades):.2f}")

    print("\n===== FINAL RESULT =====")

    if status == "PASSED":
        print("Congratulations! You passed!")
        print("Keep up the good work!")
    else:
        print("Unfortunately, you did not meet the passing grade.")
        print("Don't give up! Keep improving!")    
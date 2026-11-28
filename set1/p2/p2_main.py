# Full Name: Kate Diane Inoue
# Section: IV-BSIT B
# Activity: Set 1 - P2: Custom Module: student_utils
# Date: November 27, 2026

# import built-in and custom modules
import datetime
import student_utils
from student_utils import calc_average

# list of subjects
SUBJECTS = [
    "LN01_CAP 102 - Capstone Project 2",
    "LNO1_ELEC3 - Elective 3 (Special Topics on Web and Mobile 1)",
    "LNO1_ELEC4 - Elective 4 (Special Topics on Web and Mobile 2)",
    "LNO1_IAS 102 - Information Assurance and Security 2",
    "LNO1_SA 101 - System Administration and Maintenance",
    "LNO1_SIA 101 - System Integration and Architecture"
]

def main():
    # stores grades for each subject
    grades = {}

    print("===== ENTER YOUR GRADE FOR EACH SUBJECT =====")

    # collect and validate grades
    for subject in SUBJECTS:
        while True:
            try:
                grade = float(input(f"{subject}: "))

                if 0 <= grade <= 100:
                    grades[subject] = grade
                    break
                else:
                    print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    print("\n===== STUDENT GRADE RESULTS =====")

    # calculate average grade
    average = calc_average(grades)
    print(f"Your average grade is: {average:.2f}")

    # get highest and lowest grades
    print(f"Your highest grade is: {student_utils.get_highest_grade(grades):.2f}")
    print(f"Your lowest grade is: {student_utils.get_lowest_grade(grades):.2f}")

    print("\n===== FINAL RESULT =====")
    
    # check pass or fail status
    pass_status = student_utils.check_pass(grades)

    if pass_status == "PASSED":
        print("Congratulations! You passed!")
        print("Keep up the good work!")
    else:
        print("Unfortunately, you did not meet the passing grade.")
        print("Don't give up! Keep improving!")    

    print("\n===== REPORT DATE GENERATED =====")
    
    # display report date and time
    print(datetime.datetime.now().strftime("%B %d, %Y %I:%M %p"))

# run main function when file is executed directly
if __name__ == "__main__":
    main()

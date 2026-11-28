# Full Name: Kate Diane Inoue
# Section: IV-BSIT B
# Activity: Set 1 - P2: Custom Module: student_utils
# Date: November 27, 2026

# passing grade requirement
PASSING_GRADE = 75

# calculate average
def calc_average(grades):
    if not grades:
        return 0

    return sum(grades.values()) / len(grades)

# check pass or fail
def check_pass(grades):
    average = calc_average(grades)

    if average >= PASSING_GRADE:
        return "PASSED"
    else:
        return "FAILED"

# get highest grade
def get_highest_grade(grades):
    if not grades:
        return 0

    return max(grades.values())

# get lowest grade
def get_lowest_grade(grades):
    if not grades:
        return 0

    return min(grades.values())
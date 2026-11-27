# Full Name: Kate Diane Inoue
# Section: IV-BSIT B
# Activity: Set 1 - P2: Custom Module: student_utils
# Date: November 27, 2026

PASSING_GRADE = 75

# calculate average
def calc_average(grades):
    if not grades:
        return 0

    return sum(grades.values()) / len(grades)
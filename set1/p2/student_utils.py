
# Full Name: GALLANONGO, GILBERT B.
# Section: IV-BSIT B
# Course: ELEC 4 - Python Programming
# Activity: P2 - Custom Module
# Date: November 19, 2026

def calculate_average(grades):
    # Kinukuha ang average ng lahat ng grades.
    return sum(grades) / len(grades)

def determine_status(grades):
    # Kapag 75 pataas ang average, pasado ang student.
    average = calculate_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"

def get_highest_grade(grades):
    # Hinahanap ang pinakamataas na grade sa list.
    return max(grades)

def get_lowest_grade(grades):
    # Hinahanap ang pinakamababang grade sa list.
    return min(grades)
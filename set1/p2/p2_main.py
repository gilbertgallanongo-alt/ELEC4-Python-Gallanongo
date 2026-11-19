
# Full Name: GALLANONGO, GILBERT B.
# Section: IV-BSIT B
# Course: ELEC 4 - Python Programming
# Activity: P2 - Custom Module Main Program
# Date: November 19, 2026

# First import style: buong custom module ang ini-import.
import student_utils

# Second import style: specific functions lang ang ini-import.
from student_utils import get_highest_grade, get_lowest_grade

# Built-in module para sa date at time ng report.
from datetime import datetime

def accept_grades():
    grades = []

    # Tatanungin muna kung ilang grades ang ilalagay.
    while True:
        try:
            total = int(input("How many grades will you enter? "))

            if total > 0:
                break

            print("Please enter at least one grade.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Isa-isang kukunin at iche-check ang grades.
    for i in range(total):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1} (0-100): "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break

                print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    return grades

def display_report(grades):
    # Ginagamit ang datetime para ipakita kung kailan ginawa ang report.
    report_date = datetime.now().strftime("%B %d, %Y - %I:%M %p")

    print("\n========== STUDENT GRADE REPORT ==========")
    print("Prepared by: GALLANONGO, GILBERT B.")
    print(f"Report Generated: {report_date}")
    print("------------------------------------------")
    print(f"Grades: {grades}")

    # Gamit ang import student_utils.
    print(f"Average: {student_utils.calculate_average(grades):.2f}")
    print(f"Status: {student_utils.determine_status(grades)}")

    # Gamit ang from student_utils import ...
    print(f"Highest Grade: {get_highest_grade(grades):.2f}")
    print(f"Lowest Grade: {get_lowest_grade(grades):.2f}")
    print("==========================================")

def main():
    print("========== STUDENT GRADE REPORT ==========")
    print("Student Grade Calculator Using Modules")
    print("==========================================")

    # Tatawagin ang input function bago gumawa ng report.
    student_grades = accept_grades()

    # Ipapakita ang results gamit ang imported functions.
    display_report(student_grades)

if __name__ == "__main__":
    # Dito magsisimula ang program kapag direktang ni-run ang file.
    main()

# Full Name: GALLANONGO, GILBERT B.
# Section: IV-BSIT B
# Course: ELEC 4 - Python Programming
# Activity: P1 - Student Grade Calculator
# Date: November 18, 2026

def accept_grades():
    grades = []
    
    while True:
        try:
            number_of_grades = int(input("How many grades will you enter? "))

            if number_of_grades > 0:
                break

            print("Please enter at least one grade.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    for i in range(number_of_grades):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1} (0-100): "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break

                print("Invalid grade. Enter a value from 0 to 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    return grades

def calculate_average(grades):
    return sum(grades) / len(grades)


def get_highest_grade(grades):
    return max(grades)


def get_lowest_grade(grades):
    return min(grades)

def determine_status(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"

def display_results(grades):
    print("\n========== STUDENT GRADE RESULTS ==========")
    print(f"Grades: {grades}")
    print(f"Total Number of Grades: {len(grades)}")
    print(f"Average: {calculate_average(grades):.2f}")
    print(f"Highest Grade: {get_highest_grade(grades):.2f}")
    print(f"Lowest Grade: {get_lowest_grade(grades):.2f}")
    print(f"Status: {determine_status(grades)}")
    print("===========================================")

def main():
    student_grades = []

    while True:
        print("\n========== STUDENT GRADE CALCULATOR ==========")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")
        print("==============================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_grades = accept_grades()

        elif choice == "2":
            if student_grades:
                display_results(student_grades)
            else:
                print("No grades available. Please enter grades first.")

        elif choice == "3":
            print("Thank you for using the Student Grade Calculator!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
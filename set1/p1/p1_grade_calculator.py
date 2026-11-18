
# Full Name: GALLANONGO, GILBERT B.
# Section: IV-BSIT B
# Course: ELEC 4 - Python Programming
# Activity: P1 - Student Grade Calculator
# Date: November 18, 2026

def accept_grades():
    # Dito natin ilalagay ang lahat ng grades na i-e-enter ng user.
    grades = []

    # Hihingi tayo ng valid na bilang ng grades.
    while True:
        try:
            number_of_grades = int(input("How many grades will you enter? "))

            if number_of_grades > 0:
                break

            print("Please enter at least one grade.")

        except ValueError:
            # Kapag hindi whole number ang input, magtatanong ulit.
            print("Invalid input. Please enter a whole number.")

    # Isa-isang tatanggapin at iche-check ang bawat grade.
    for i in range(number_of_grades):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1} (0-100): "))

                # Tatanggapin lang ang grade kapag nasa 0 hanggang 100.
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break

                print("Invalid grade. Enter a value from 0 to 100.")

            except ValueError:
                # Kapag text o invalid number ang nilagay, magre-repeat.
                print("Invalid input. Please enter a number.")

    return grades

def calculate_average(grades):
    # Kinukuha ang total ng grades at hinahati sa dami nito.
    return sum(grades) / len(grades)

def get_highest_grade(grades):
    # Ibinabalik ang pinakamataas na grade.
    return max(grades)

def get_lowest_grade(grades):
    # Ibinabalik ang pinakamababang grade.
    return min(grades)

def determine_status(grades):
    # Iche-check kung pasado o bagsak base sa average na 75.
    average = calculate_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"

def display_results(grades):
    # Dito ipapakita ang summary ng grades ng student.
    print("\n========== STUDENT GRADE RESULTS ==========")
    print(f"Grades: {grades}")
    print(f"Total Number of Grades: {len(grades)}")
    print(f"Average: {calculate_average(grades):.2f}")
    print(f"Highest Grade: {get_highest_grade(grades):.2f}")
    print(f"Lowest Grade: {get_lowest_grade(grades):.2f}")
    print(f"Status: {determine_status(grades)}")
    print("===========================================")

def main():
    # Local variable ito na nagtatago ng grades habang tumatakbo ang program.
    student_grades = []

    # Paulit-ulit na ipapakita ang menu hanggang piliin ang Exit.
    while True:
        print("\n========== STUDENT GRADE CALCULATOR ==========")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")
        print("==============================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Tatawagin ang function para mag-enter ng grades.
            student_grades = accept_grades()

        elif choice == "2":
            # Ipapakita lang ang results kung may na-enter nang grades.
            if student_grades:
                display_results(student_grades)
            else:
                print("No grades available. Please enter grades first.")

        elif choice == "3":
            print("Thank you for using the Student Grade Calculator!")
            break

        else:
            # Kapag hindi 1, 2, o 3 ang pinili, babalik sa menu.
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    # Dito magsisimula ang program sa pamamagitan ng main() function.
    main()

# LOCAL AND GLOBAL VARIABLES
# Ang local variable ay ginawa sa loob ng isang function at doon lang ito accessible.
# Halimbawa, ang student_grades ay local variable sa loob ng main() function.
# Ang global variable naman ay dineclare sa labas ng functions at puwedeng gamitin sa iba't ibang functions.
# Sa program na ito, hindi natin kailangan ng global variable dahil ipinapasa natin ang grades gamit ang parameters at return values.
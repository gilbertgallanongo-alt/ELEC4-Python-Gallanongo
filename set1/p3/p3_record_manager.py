# Name: GALLANONGO, GILBERT B.
# Section: IV-BSIT B
# ELEC 4 - P3 Student Record Manager
# Date: November 20, 2026

# Dito muna naka-save yung mga student.
# List para sa names, set para walang doble.
students = []
student_names = set()

def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    # Check muna kung nasa records na.
    name_key = name.casefold()

    if name_key in student_names:
        print("Student already exists.")
    else:
        students.append(name)
        student_names.add(name_key)
        print(f"{name} added successfully.")

def remove_student():
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.casefold() == name.casefold():
            students.remove(student)
            student_names.remove(student.casefold())

            print(f"{student} removed successfully.")
            return

    print("Student not found.")

def search_student():
    # Kahit part lang ng name, pwede na.
    keyword = input("Enter name to search: ").strip()

    if not keyword:
        print("Please enter a name.")
        return

    found = False

    for student in students:
        if keyword.lower() in student.lower():
            print(f"Found: {student}")
            found = True

    if not found:
        print("No student found.")

def display_students():
    print("\n========== STUDENT RECORDS ==========")

    if not students:
        print("No student records yet.")
    else:
        # Para alphabetical yung display.
        sorted_students = sorted(students, key=str.casefold)

        for number, name in enumerate(sorted_students, start=1):
            print(f"{number}. {name}")

    print(f"Total Students: {len(students)}")
    print("=====================================")

def main():
    # Dito lang umiikot yung menu.
    while True:
        print("\n========== STUDENT RECORD MANAGER ==========")
        print("Prepared by: GALLANONGO, GILBERT B.")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display Students")
        print("5. Exit")
        print("============================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Exiting Student Record Manager...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


# Yung list, ginagamit ko para ma-save yung names ng students.
# Pwede kasing maulit ang values sa list.
# Yung set naman, hindi nag-aallow ng duplicate values.
# Ginamit ko yung set para ma-check kung may kaparehong name na.
# Kaya parehong useful yung list at set sa program na ito.
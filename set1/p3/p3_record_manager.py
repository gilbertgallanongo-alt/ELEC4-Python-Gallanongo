# Name: GALLANONGO, GILBERT B.
# Section: IV-BSIT B
# ELEC 4 - P3 Student Record Manager
# Date: November 20, 2026

# Dito muna naka-save yung mga student.
students = []

def add_student():
    # Kuha lang ng name na ia-add.
    name = input("Enter student name: ").strip()

    if name:
        students.append(name)
        print(f"{name} added successfully.")
    else:
        print("Student name cannot be empty.")

def remove_student():
    # Hanapin yung name bago tanggalin.
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.lower() == name.lower():
            students.remove(student)
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
    # Para makita lahat ng nasa list.
    print("\n========== STUDENT RECORDS ==========")

    if not students:
        print("No student records yet.")
    else:
        for number, name in enumerate(students, start=1):
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
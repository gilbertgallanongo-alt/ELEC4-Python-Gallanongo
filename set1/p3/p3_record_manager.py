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
    # Babalik lang sa menu hangga't hindi nag-eexit.
    while True:
        print("\n========== STUDENT RECORD MANAGER ==========")
        print("Prepared by: GALLANONGO, GILBERT B.")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")
        print("============================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            print("Exiting Student Record Manager...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
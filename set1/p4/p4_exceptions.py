# Name: GALLANONGO, GILBERT B.
# Section: IV-BSIT B
# ELEC 4 - P4 Safe Menu Program
# Date: November 21, 2026

def divide_numbers():
    print("\n========== DIVISION ==========")

    try:
        # Kumuha ng dalawang numbers.
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 / num2

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    else:
        print(f"Result: {result}")

    finally:
        print("Division process finished.")

def main():
    while True:
        print("\n========== SAFE MENU PROGRAM ==========")
        print("1. Divide Two Numbers")
        print("2. Open a Text File")
        print("3. Exit")
        print("=======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            divide_numbers()

        elif choice == "2":
            print("File reading will be added in the next commit.")

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid menu choice. Please try again.")

if __name__ == "__main__":
    main()
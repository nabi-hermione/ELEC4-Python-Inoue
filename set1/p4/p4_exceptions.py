# Full Name: Kate Diane Inoue
# Section: IV-BSIT B
# Activity: Set 1 - P4: Safe Menu Program
# Date: November 28, 2026

# perform division with exception handling
def divide_numbers():
    try:
        while True:
            try:
                num1 = float(input("Enter first number: "))
                break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

        while True:
            try:
                num2 = float(input("Enter second number: "))
                result = num1 / num2

            except ValueError:
                print("Invalid input. Please enter numbers only.")

            except ZeroDivisionError:
                print("Cannot divide by zero.")

            else:
                print(f"Result: {result:.2f}")
                break

    finally:
        print("Division operation completed.")

# read and display file contents
def read_file():
    file_name = input("Enter file name: ").strip()

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print("File not found. Please check the file name.")

    else:
        print("\n===== FILE CONTENTS =====")
        print(content)
        print("File reading operation completed.")
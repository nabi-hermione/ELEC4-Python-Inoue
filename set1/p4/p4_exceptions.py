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
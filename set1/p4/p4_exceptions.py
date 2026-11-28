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

# display menu and handle user choices
def main():
    while True:
        print("\n===== SAFE MENU PROGRAM =====")
        print("1. Divide Numbers")
        print("2. Open File")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            divide_numbers()
        elif choice == "2":
            read_file()
        elif choice == "3":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Please select from 1 to 3.")

# run main function when file is executed directly
if __name__ == "__main__":
    main()

# Ang exception handling ay ginagamit para ma-handle ang mga errors na maaaring mangyari
# habang tumatakbo ang program para hindi basta mag-stop kapag may invalid na input.
# Ang try block ay kung saan nilalagay yung code na posibleng magkaroon ng error.
# Kapag may letters or invalid na number na in-enter ang user, ang ValueError ang magha-handle nito.
# Kapag naman nag-enter ng zero sa second number during division, ZeroDivisionError ang magha-handle.
# Sa file reading naman, kapag hindi makita yung file na hinahanap ng user,
# FileNotFoundError ang magbibigay ng error message.
# Ang except ay ginagamit para mahuli at ma-handle yung specific error.
# Kapag else naman, ie-execute lang ito kapag walang error na nangyari sa try block.
# Ang finally ay laging nage-execute kahit may error or wala.
# In summary, ang exception handling ay tumutulong para maging maayos ang takbo ng program
# kahit may maling input or missing file. Instead na mag-crash agad ang program,
# nagbibigay ito ng appropriate error message and allows the user to continue.
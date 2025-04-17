def check_eligibility():
    current_year = 2025
    birth_year = int(input("Enter your birth year: "))
    age = current_year - birth_year
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

if __name__ == "__main__":
    check_eligibility()


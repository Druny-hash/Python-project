# Constants for rates
BONUS_RATE = 0.40
ALLOWANCE_RATE = 0.05
PF_RATE = 0.10
TAX_RATE = 0.01
ADVANCE = 5000  # Fixed deduction

def get_valid_salary():
    """Prompt the user for a valid base salary."""
    while True:
        try:
            salary = float(input("Enter base salary: "))
            if salary < 0:
                print("Salary cannot be negative. Please enter a valid amount.")
            else:
                return salary
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Get valid base salary from the user
salary = get_valid_salary()

# Calculations
bonus = BONUS_RATE * salary
allowance = ALLOWANCE_RATE * salary
pf = PF_RATE * salary
tax = TAX_RATE * salary

total_salary = salary + bonus + allowance
net_salary = total_salary - (pf + tax + ADVANCE)

# Output
print("\n--- Salary Breakdown ---")
print(f"Base Salary         : Rs. {salary:,.2f}")
print(f"Bonus ({BONUS_RATE*100:.0f}%)      : Rs. {bonus:,.2f}")
print(f"Allowance ({ALLOWANCE_RATE*100:.0f}%): Rs. {allowance:,.2f}")
print(f"Provident Fund ({PF_RATE*100:.0f}%): Rs. {pf:,.2f}")
print(f"Tax ({TAX_RATE*100:.0f}%)          : Rs. {tax:,.2f}")
print(f"Advance             : Rs. {ADVANCE:,.2f}")
print(f"Total Salary        : Rs. {total_salary:,.2f}")
print(f"Net Salary          : Rs. {net_salary:,.2f}")
salary = float(input("Enter base salary: "))

bonus = 0.40 * salary
allowance = 0.05 * salary
pf = 0.10 * salary
tax = 0.01 * salary
advance = 5000  # Fixed

total_salary = salary + bonus + allowance
net_salary = total_salary - (pf + tax + advance)


print("\n--- Salary Breakdown ---")
print(f"Base Salary     : Rs. {salary:.2f}")
print(f"Bonus (40%)     : Rs. {bonus:.2f}")
print(f"Allowance (5%)  : Rs. {allowance:.2f}")
print(f"Provident Fund (10%): Rs. {pf:.2f}")
print(f"Tax (1%)        : Rs. {tax:.2f}")
print(f"Advance         : Rs. {advance:.2f}")
print(f"Total Salary    : Rs. {total_salary:.2f}")
print(f"Net Salary      : Rs. {net_salary:.2f}")

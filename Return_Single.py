# This program simulates a bank system
# The function calculates interest earned and returns a single value

def calculate_interest(principal, rate, time):
    # Formula: Interest = Principal × Rate × Time
    interest = principal * rate * time
    return interest  # Returning a single value

# Ask user for input
principal_amount = float(input("Enter principal amount: "))
annual_rate = float(input("Enter annual interest rate (in decimal, e.g., 0.05 for 5%): "))
years = int(input("Enter time in years: "))

# Call the function and store the return value
earned_interest = calculate_interest(principal_amount, annual_rate, years)

# Display result
print(f"\nInterest earned after {years} years: {earned_interest}")

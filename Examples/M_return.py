# Function that calculates new balance and returns multiple values
def withdraw(balance, amount):
    new_balance = balance - amount
    transaction_status = "Success" if amount <= balance else "Failed"
    return new_balance, transaction_status  # multiple return values

# User input
current_balance = float(input("Enter your current balance: "))
withdraw_amount = float(input("Enter amount to withdraw: "))

# Function call
updated_balance, status = withdraw(current_balance, withdraw_amount)

# Display result
print(f"\nTransaction Status: {status}")
print(f"Updated Balance: ₱{updated_balance}")

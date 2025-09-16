# Function that calculates new balance after withdrawal
def withdraw(balance, amount):
    new_balance = balance - amount
    return new_balance   # returns a single value

# User input
current_balance = float(input("Enter your current balance: "))
withdraw_amount = float(input("Enter amount to withdraw: "))

# Function call
updated_balance = withdraw(current_balance, withdraw_amount)

# Display result
print(f"\nTransaction successful! Your new balance is: ₱{updated_balance}")

# This program simulates an ATM receipt printer
# The function only prints a receipt, it does not return any value
# Therefore, Python automatically returns None

def print_receipt(user, amount, balance):
    print("\n------ ATM RECEIPT ------")
    print(f"Account Holder: {user}")
    print(f"Withdrawn Amount: ₱{amount}")
    print(f"Remaining Balance: ₱{balance}")
    print("-------------------------")

# Ask user for input
name = input("Enter account holder name: ")
withdraw = float(input("Enter amount to withdraw: "))
balance = float(input("Enter current balance: "))

# Call the function
result = print_receipt(name, withdraw, balance)

# Check what the function returned
print("Function returned:", result)

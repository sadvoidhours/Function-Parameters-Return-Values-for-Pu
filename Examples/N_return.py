# Function that only prints a receipt, does not return a value
def print_receipt(user, amount, balance):
    print("\n------ BANK RECEIPT ------")
    print(f"Account Holder: {user}")
    print(f"Withdrawn Amount: ₱{amount}")
    print(f"Remaining Balance: ₱{balance}")
    print("--------------------------")
    # No return statement → Python returns None automatically

# User input
name = input("Enter account holder name: ")
withdraw = float(input("Enter amount to withdraw: "))
balance = float(input("Enter current balance: "))

# Call the function
result = print_receipt

# Function that accepts parameters
def place_order(item, quantity, address):
    print(f"\nOrder Details:")
    print(f"Item: {item}")
    print(f"Quantity: {quantity}")
    print(f"Delivery Address: {address}")

# User input
item_name = input("Enter the item name: ")
qty = int(input("Enter the quantity: "))
addr = input("Enter delivery address: ")

# Function call using keyword arguments (order doesn't matter)
place_order(item=item_name, quantity=qty, address=addr)

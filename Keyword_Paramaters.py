# This program simulates an online shopping checkout system
# Keyword parameters make it clear which value belongs to which parameter

def checkout(item, price, quantity, buyer):
    total = price * quantity
    print(f"\nOrder Summary for {buyer}:")
    print(f"Item: {item}")
    print(f"Price: {price} x {quantity}")
    print(f"Total Amount: {total}")

# Main loop
while True:
    # Ask user for input
    item_name = input("Enter item name: ")
    item_price = float(input("Enter item price: "))
    item_quantity = int(input("Enter quantity: "))
    buyer_name = input("Enter buyer name: ")

    # Call the function using keyword arguments
    checkout(item=item_name, price=item_price, quantity=item_quantity, buyer=buyer_name)
    
    # Ask if user wants to continue
    continue_shopping = input("\nDo you want to process another order? (y/n): ").lower()
    if continue_shopping != 'y':
        print("Thank you for using the checkout system!")
        break

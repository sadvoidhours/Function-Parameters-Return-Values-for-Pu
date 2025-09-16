# This program simulates a restaurant ordering system
# The function 'place_order' uses positional parameters
# The user inputs food, drink, and table number which are passed to the function in order

# List to store all orders
all_orders = []

# Function with positional parameters
def place_order(food, drink, table_number):
    # Display the order details
    print(f"\nOrder received: {food} with {drink}")
    print(f"Deliver to table {table_number}")
    
    # Store the order in the list
    order = {"food": food, "drink": drink, "table": table_number}
    all_orders.append(order)

# Function to display all orders
def display_all_orders():
    if not all_orders:
        print("\nNo orders placed yet.")
        return
    
    print("\n--- All Orders ---")
    for i, order in enumerate(all_orders, 1):
        print(f"{i}. {order['food']} with {order['drink']} - Table {order['table']}")

# Main program loop
while True:
    print("\n--- Restaurant Order System ---")
    print("1. Place an order")
    print("2. Display all orders")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        # Ask user for input (simulating a customer placing an order)
        food_item = input("Enter the food item: ")      # Example: Pizza
        drink_item = input("Enter the drink: ")        # Example: Coke
        table_num = int(input("Enter the table number: "))  # Example: 7
        
        # Call the function with the values provided by the user
        # The order of arguments is important because this is a positional parameter example
        place_order(food_item, drink_item, table_num)
        
    elif choice == "2":
        display_all_orders()
        
    elif choice == "3":
        print("\nThank you for using the restaurant order system!")
        break
        
    else:
        print("\nInvalid option. Please choose 1, 2, or 3.")

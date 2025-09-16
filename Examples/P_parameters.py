# Function that takes parameters in a specific order (positional parameters)
def order_food(item, quantity):
    print(f"You ordered {quantity} {item}(s).")

# User input
food = input("Enter the food item: ")
qty = int(input("Enter the quantity: "))

# Function call (order matters: item first, then quantity)
order_food(food, qty)

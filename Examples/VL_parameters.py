# Function that accepts both *args (items) and **kwargs (details)
def place_order(*items, **details):
    print("\n Items in your order:")
    for item in items:
        print(f"- {item}")

    print("\n Delivery Details:")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

# Example usage
place_order(
    "Laptop", "Mouse", "Headset",      # *args (items)
    name="Mark", city="Manila", address="123 Main Street", payment="COD"  # **kwargs (details)
)

# This program simulates a travel booking system with default parameters
# If the user does not provide input, the booking will use default values
# Now supports multiple users with exit option

def book_trip(destination="Manila", seat_class="Economy", user_name="Guest"):
    print(f"\nTrip booked for {user_name} to {destination} in {seat_class} class.")

def main():
    print("Welcome to the Travel Booking System!")
    print("=" * 40)
    
    while True:
        print("\n--- New Booking ---")
        
        # Get user name
        user_name = input("Enter your name: ").strip() or "Guest"
        
        # Ask user for input
        dest = input("Enter destination (press Enter for default Manila): ").strip() or "Manila"
        seat = input("Enter seat class (press Enter for default Economy): ").strip() or "Economy"
        
        # Call the function with user input (or defaults)
        book_trip(dest, seat, user_name)
        
        # Ask if user wants to continue
        print("\nOptions:")
        print("1. Book another trip")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ").strip()
        
        if choice == "2":
            print("\nThank you for using our booking system. Goodbye!")
            break
        elif choice != "1":
            print("Invalid choice. Continuing with new booking...")

# Run the main program
if __name__ == "__main__":
    main()

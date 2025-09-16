# Function with a default parameter for seat type
def book_ticket(movie, seat_type="Regular"):
    print(f"Booking confirmed for '{movie}' in {seat_type} seat.")

# User input
movie_name = input("Enter the movie name: ")

# Optionally, user can input seat type
choice = input("Do you want to choose seat type? (yes/no): ").lower()

if choice == "yes":
    seat = input("Enter seat type (Regular/VIP): ")
    book_ticket(movie_name, seat)  # Uses user input
else:
    book_ticket(movie_name)        # Uses default value

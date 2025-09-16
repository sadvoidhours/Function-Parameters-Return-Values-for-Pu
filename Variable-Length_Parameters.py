# This program simulates a student registration system
# *args is used for multiple courses
# **kwargs is used for student details (like age, year, section)

# Global storage for students
students_database = {}
id_counter = 1

def generate_student_id():
    """Generate student ID in format TUPT-25-xxxx"""
    global id_counter
    student_id = f"TUPT-25-{id_counter:04d}"
    id_counter += 1
    return student_id

def register_student(*courses, **details):
    """Register a new student and return their ID"""
    student_id = generate_student_id()
    
    print(f"\n--- Student Registration Summary ---")
    print(f"Student ID: {student_id}")
    
    # Show courses
    if courses:
        print("Enrolled Courses:", ", ".join(courses))
    else:
        print("Enrolled Courses: None")
    
    # Show student details
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")
    
    # Store student in database
    students_database[student_id] = {
        'courses': list(courses),
        'details': details
    }
    
    print(f"✓ Student {details.get('name', 'Unknown')} registered successfully!")
    return student_id

def display_all_students():
    """Display all registered students"""
    if not students_database:
        print("\nNo students registered yet.")
        return
    
    print(f"\n--- All Registered Students ({len(students_database)} total) ---")
    for student_id, data in students_database.items():
        print(f"\nStudent ID: {student_id}")
        for key, value in data['details'].items():
            print(f"{key.capitalize()}: {value}")
        if data['courses']:
            print("Enrolled Courses:", ", ".join(data['courses']))
        else:
            print("Enrolled Courses: None")
        print("-" * 30)

def delete_student():
    """Delete a student by ID"""
    if not students_database:
        print("\nNo students to delete.")
        return
    
    print("\nRegistered Student IDs:")
    for student_id in students_database.keys():
        name = students_database[student_id]['details'].get('name', 'Unknown')
        print(f"- {student_id} ({name})")
    
    student_id = input("\nEnter Student ID to delete: ").strip().upper()
    
    if student_id in students_database:
        name = students_database[student_id]['details'].get('name', 'Unknown')
        del students_database[student_id]
        print(f"✓ Student {name} ({student_id}) deleted successfully!")
    else:
        print("Student ID not found.")

def get_student_input():
    """Get student registration input from user"""
    print("\n--- New Student Registration ---")
    print("Enter the courses (separated by commas, leave blank if none):")
    courses_input = input("Courses: ")
    courses_list = [c.strip() for c in courses_input.split(",") if c.strip()]

    name = input("Enter student name: ")
    age = input("Enter student age: ")
    year = input("Enter year level: ")
    section = input("Enter section: ")
    
    return courses_list, name, age, year, section

def main():
    """Main program loop"""
    print("🎓 Student Registration System")
    print("=" * 40)
    
    while True:
        print("\n--- MENU ---")
        print("1. Register New Student")
        print("2. Display All Students")
        print("3. Delete Student")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            courses_list, name, age, year, section = get_student_input()
            register_student(*courses_list, name=name, age=age, year=year, section=section)
        
        elif choice == '2':
            display_all_students()
        
        elif choice == '3':
            delete_student()
        
        elif choice == '4':
            print("\nThank you for using the Student Registration System!")
            break
        
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")

# Run the program
if __name__ == "__main__":
    main()

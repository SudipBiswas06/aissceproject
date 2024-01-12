from student_details import StudentDetails
from student_marks import StudentMarks
from report_card_format import ReportCard

# Create instances of the required classes
details = StudentDetails()
marks = StudentMarks()
report = ReportCard()

# Use a while loop to allow the user to continue using the program
ans = "yes"
while ans in ['y', 'Y', 'yes', 'Yes']:
    print("   Student Report Card Management System")
    print("1. Enter Student Details")
    print("2. Display Specific Student Details")
    print("3. Display All Student Details")
    print("4. Enter Student Marks")
    print("5. Display Specific Student Marks")
    print("6. Display All Student Marks")
    print("7. Show Report Card of Specific Student")
    print("8. Show Report Card of All Students")
    print("9. Exit")
    
    # Prompt the user to enter their choice
    choice = input("Enter your choice(1-9): ")
    
    # Use if-elif-else statements to handle the user's choice
    if choice == "1":
        details.set_student_details()
    elif choice == "2":
        details.show_student_details()
    elif choice == "3":
        details.show_all_student_details()
    elif choice == "4":
        marks.add_marks()
    elif choice == "5":
        marks.show_marks_of_single_student()
    elif choice == "6":
        marks.show_marks_of_all_students()
    elif choice == "7":
        report.generate_report_card_for_student()
    elif choice == "8":
        report.generate_report_card_for_all_students()
    elif choice == "9":
        print("Thank You!!! For using Student Database Management")
        break
    else:
        print("Invalid choice. Please try again.")
    
    # Prompt the user to continue or exit the program
    ans = input("Do you want to continue? (yes/no): ")
    if ans not in ['y', 'Y', 'yes', 'Yes']:
        print("Thank You!!! For using Student Database Management")
        break

    print()
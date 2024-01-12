import csv
import os

class StudentDetails:
    def __init__(self):
        self.name = ""
        self.admission_no = ""
        self.Class = 0
        self.stream = ""
        self.roll_number = 0


    def set_student_details(self):
        # Check if the CSV file exists, if not create it
        if not os.path.exists("students_details.csv"):
            with open("students_details.csv", "w", newline="") as file:
                pass

        # Prompt the user to enter student details
        self.name = input("Enter Name: ").title()  # Capitalize first letter of each word
        self.admission_no = input("Enter Admission Number: ")
        self.Class = int(input("Enter Class: "))
        self.stream = input("Enter Stream (Science/Arts/Commerce): ").title()  # Capitalize first letter of each word
        self.roll_number = int(input("Enter Roll Number: "))

        # Append the student details to the CSV file
        with open("students_details.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.roll_number, self.admission_no, self.name, self.Class, self.stream])
        print("Student created successfully!")
        print()


    def show_student_details(self):
        # Check if the CSV file exists
        if not os.path.exists("students_details.csv"):
            print("No student details found.")
            return

        # Prompt the user to enter roll number and stream to search for a student
        with open("students_details.csv", "r") as file:
            reader = csv.reader(file)
            self.roll_number = int(input("Enter roll number of the student: "))
            self.stream = input("Enter stream of the student (Science/Arts/Commerce): ").title()
            for row in reader:
                if int(row[0]) == self.roll_number and row[4] == self.stream:
                    # Display the matching student details
                    print("-" * 30)
                    print("Name:", row[2])
                    print("Admission Number:", row[1])
                    print("Class:", row[3])
                    print("Stream:", row[4])
                    print("Roll Number:", row[0])
                    print("-" * 30)
                    print()
                    break
            else:
                print("No student details found with the given roll number and stream.")
                print()


    def show_all_student_details(self):
    # Check if the CSV file exists
        if not os.path.exists("students_details.csv"):
            print("No student details found.")
            return

        # Display details of all students in the CSV file
        with open("students_details.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                # Display the details for each student
                print("-" * 30)
                print("Name:", row[2])
                print("Admission Number:", row[1])
                print("Class:", row[3])
                print("Stream:", row[4])
                print("Roll Number:", row[0])
                print("-" * 30)
                print()


if __name__ == "__main__":
    details = StudentDetails()
    details.set_student_details()
    details.show_student_details()
    details.show_all_student_details()
import csv
import os

class StudentMarks:
    def __init__(self):
        # Initialize class variables
        self.marks = {}
        self.marks_obtained = []
        self.total_marks = 0
        self.percentage = 0.0
        self.grade = ""
        self.result = ""
        self.name = ""
        self.roll_number = 0
        self.stream = ""
        self.performance = ""


    def add_marks(self):
        # Check if the CSV file exists, if not create it
        if not os.path.exists("students_marks.csv"):
            with open("students_marks.csv", "w", newline="") as file:
                pass

        # Prompt the user to enter student details
        self.name = input("Enter student name: ").title()
        self.roll_number = int(input("Enter roll number: "))
        self.stream = input("Enter the stream (Science/Arts/Commerce): ").title()

        # Determine the subjects based on the stream
        if self.stream.title() == "Science":
            subjects = ["Physics", "Chemistry", "Mathematics", "English", "Computer Science"]
        elif self.stream.title() == "Arts":
            subjects = ["History", "Geography", "English", "Political Science", "Economics"]
        elif self.stream.title() == "Commerce":
            subjects = ["Accountancy", "Business Studies", "Economics", "English", "Information Technology"]
        else:
            print("Invalid stream entered. Please try again.")
            return

        # Prompt the user to enter marks for each subject and store them in the marks dictionary
        marks_obtained = []
        for subject in subjects:
            marks = int(input("Enter the marks for {}: ".format(subject)))
            self.marks[subject] = marks
            marks_obtained.append(f"{subject}- {marks}")

        # Calculate total marks and percentage
        total_marks = sum(self.marks.values())
        percentage = (total_marks / (len(subjects) * 100)) * 100

        # Determine the grade based on the percentage
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        elif percentage >= 40:
            grade = "E"
        else:
            grade = "F"

        # Determine the result based on the grade
        if grade != "F":
            result = "PASS"
        else:
            result = "FAIL"

        # Determine the performance based on the grade
        if grade == "A+":
            performance = "Excellent, Keep it up!"
        elif grade == "A":
            performance = "Very Good, Continue Improving!"
        elif grade == "B":
            performance = "Well Done, Can do better!"
        elif grade == "C":
            performance = "Good, Need to work a little bit harder!"
        elif grade == "D":
            performance = "Needs Improvement, Work on it!"
        elif grade == "E":
            performance = "Needs Improvement, Work Harder!"
        else:
            performance = "Fail, Better Luck Next Time!"

        # Write the student details to the CSV file
        with open("students_marks.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.roll_number, self.name, self.stream] + marks_obtained + [total_marks, f"{percentage:.2f}%", grade, result, performance])
            print("Marks added successfully!")
            print()



    def show_marks_of_single_student(self):
        # Check if the 'students_marks.csv' file exists
        if not os.path.exists("students_marks.csv"):
            print("No student details found.")
            return
        
        with open("students_marks.csv", "r") as marks_file:
            marks_reader = csv.reader(marks_file)
            
            # Get user input for roll number and stream
            self.roll_number = int(input("Enter roll number of the student: "))
            self.stream = input("Enter stream of the student (Science/Arts/Commerce): ").title()
            
            for row in marks_reader:
                # Check if the roll number and stream match the current row
                if int(row[0]) == self.roll_number and row[2] == self.stream:
                    print()
                    print('-'*30)
                    print("Name:", row[1])
                    print("Roll Number:", row[0])
                    print("Stream:", row[2])
                    print("-------------------------")
                    print("Marks Obtained:")
                    subjects = row[3:-5]
                    for subject in subjects:
                        subject_name, marks_obtained = subject.split("-")
                        subject_name = subject_name.strip()
                        marks_obtained = marks_obtained.strip()
                        print(f"{subject_name}: {marks_obtained}")
                    print("-------------------------")
                    print("Total Marks:", row[-5])
                    print("Percentage:", row[-4])
                    print("Grade:", row[-3])
                    print("Result:", row[-2])
                    print('-'*30)
                    print()
                    break
            else:
                print("No student marks found with the given roll number and stream.")
                print()


    def show_marks_of_all_students(self):
        # Check if the 'students_marks.csv' file exists
        if not os.path.exists("students_marks.csv"):
            print("No student details found.")
            return

        with open("students_marks.csv", "r") as file:
            reader = csv.reader(file)

            # Check if the file is empty
            if os.stat("students_marks.csv").st_size == 0:
                print("No student details found.")
            else:
                for row in reader:
                    print()
                    print('-'*30)
                    print("Name:", row[1])
                    print("Roll Number:", row[0])
                    print("Stream:", row[2])
                    print("-------------------------")
                    print("Marks Obtained:")
                    subjects = row[3:-5]
                    for subject in subjects:
                        subject_name, marks_obtained = subject.split("-")
                        subject_name = subject_name.strip()
                        marks_obtained = marks_obtained.strip()
                        print(f"{subject_name}: {marks_obtained}")
                    print("-------------------------")
                    print("Total Marks:", row[-5])
                    print("Percentage:", row[-4])
                    print("Grade:", row[-3])
                    print("Result:", row[-2])
                    print('-'*30)
                    print()


if __name__ == "__main__":
    student = StudentMarks()
    student.add_marks()
    student.show_marks_of_single_student()
    student.show_marks_of_all_students()
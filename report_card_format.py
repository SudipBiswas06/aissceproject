import csv


class ReportCard:
    def __init__(self):
        self.roll_number = 0
        self.name = ""
        self.stream = ""
        self.admission_no = ""

    def get_student_details(self):
        # Prompt the user to enter the roll number and stream of the student
        self.roll_number = int(input("Enter roll number of the student: "))
        self.stream = input("Enter stream of the student (Science/Arts/Commerce): ").title()

    def get_student_details_stremwise(self):
        # Prompt the user to enter the stream of the student
        self.stream = input("Enter stream of the student (Science/Arts/Commerce): ").title()

    def check_empty_csv(self, file_path):
        # Check if a CSV file is empty
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            return len(list(reader)) == 0

    def print_report_card(self, row):
        # Print the report card for a single student
        print()
        print(f"    REPORT CARD OF {row[2].upper()}")
        print("-" * 30)
        print("Name:", row[2])
        print("Admission Number:", row[1])
        print("Class:", row[3])
        print("Stream:", row[4])
        print("Roll Number:", row[0])


    def generate_report_card_for_student(self):
        details_file_path = "students_details.csv"
        marks_file_path = "students_marks.csv"

        if self.check_empty_csv(details_file_path):
            print("No student details entered.")
            return

        if self.check_empty_csv(marks_file_path):
            print("No student marks entered.")
            return

        self.get_student_details()

        with open(details_file_path, "r") as details_file, \
                open(marks_file_path, "r") as marks_file:

            details_reader = csv.reader(details_file)
            marks_reader = csv.reader(marks_file)

            for row in details_reader:
                if int(row[0]) == self.roll_number and row[4] == self.stream:
                    self.print_report_card(row)
                    break
            else:
                print("No student details found with the given roll number and stream.")

            for row in marks_reader:
                if int(row[0]) == self.roll_number and row[2] == self.stream:
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
                    print("-------------------------")
                    print("Remarks: ", row[-1])
                    print('-' * 30)
                    print()
                    break
            else:
                print("No student marks found with the given roll number and stream.")


    def generate_report_card_for_all_students(self):
        details_file_path = "students_details.csv"
        marks_file_path = "students_marks.csv"

        if self.check_empty_csv(details_file_path):
            print("No student details found.")
            return

        if self.check_empty_csv(marks_file_path):
            print("No student marks found.")
            return

        with open(details_file_path, "r") as details_file, \
                open(marks_file_path, "r") as marks_file:

            details_reader = csv.reader(details_file)
            marks_reader = csv.reader(marks_file)

            for row in details_reader:
                self.print_report_card(row)

                for row in marks_reader:
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
                    print("-------------------------")
                    print("Remarks: ", row[-1])
                    print('-' * 30)
                    print()
                    break


if __name__ == "__main__":
    report = ReportCard()
    report.generate_report_card_for_student()
    report.generate_report_card_for_all_students()
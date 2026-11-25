
import csv

# Read student data from CSV file
with open("student_scores.csv", "r") as file:
    reader = csv.DictReader(file)

    print("\n===== STUDENT EXAM SCORE ANALYSIS =====")

    for student in reader:
        name = student["Name"]

        # Calculate total marks
        total = (
            int(student["Math"]) +
            int(student["Science"]) +
            int(student["English"]) +
            int(student["Computer"]) +
            int(student["History"])
        )

        # Calculate percentage
        percentage = total / 5

        # Calculate grade
        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"

        # Pass or fail
        result = "Pass" if percentage >= 40 else "Fail"

        print("--------------------------------")
        print("Student Name:", name)
        print("Total Marks:", total, "/ 500")
        print("Percentage:", round(percentage, 2), "%")
        print("Grade:", grade)
        print("Result:", result)

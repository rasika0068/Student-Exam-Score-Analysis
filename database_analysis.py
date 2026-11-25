
import mysql.connector
from getpass import getpass

# Connect to MySQL database
try:
    password = getpass("Enter MySQL student_app password: ")

    connection = mysql.connector.connect(
        host="localhost",
        user="student_app",
        password=password,
        database="student_analysis"
    )

    if connection.is_connected():
        print("\nMySQL Database Connected Successfully!")

        cursor = connection.cursor()

        # Retrieve student records
        cursor.execute("SELECT * FROM students")
        records = cursor.fetchall()

        print("\n===== STUDENT EXAM SCORE ANALYSIS =====")

        for student in records:
            student_id, name, math, science, english, computer, history = student

            total = math + science + english + computer + history
            percentage = total / 5

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

            result = (
                "Pass"
                if all(mark >= 40 for mark in
                       [math, science, english, computer, history])
                else "Fail"
            )

            print("--------------------------------")
            print("Student ID:", student_id)
            print("Student Name:", name)
            print("Total Marks:", total, "/ 500")
            print("Percentage:", round(percentage, 2), "%")
            print("Grade:", grade)
            print("Result:", result)

        cursor.close()
        connection.close()

except mysql.connector.Error as error:
    print("MySQL Error:", error)

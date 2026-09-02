import numpy as np


def calculate_grade(average):
    if average >= 90:
        return "A+"

    elif average >= 80:
        return "A"

    elif average >= 70:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    else:
        return "F"


def calculate_status(average):
    if average >= 50:
        return "Pass"

    return "Fail"


def calculate_attendance_status(attendance):
    if attendance >= 90:
        return "Excellent"

    elif attendance >= 80:
        return "Good"

    elif attendance >= 75:
        return "Warning"

    return "Critical"


def display_student(student, subjects):
    print("\n================================")
    print("        STUDENT PROFILE")
    print("================================")

    print("Student ID:", student["student_id"])
    print("Name:", student["name"])
    print("Class:", student["class_name"])
    print("Age:", student["age"])
    print("Attendance:", student["attendance"], "%")

    print("\nCurrent Marks:")

    for subject in subjects:
        print(
            subject,
            ":",
            student["subjects"][subject]
        )

    print("\nPrevious Marks:")

    for subject in subjects:
        print(
            subject,
            ":",
            student["previous_marks"][subject]
        )

    print("================================")


def generate_result(student, subjects):
    marks = np.array([
        student["subjects"][subject]
        for subject in subjects
    ], dtype=float)

    total = np.sum(marks)
    average = np.mean(marks)
    grade = calculate_grade(average)
    status = calculate_status(average)
    attendance_status = calculate_attendance_status(
        student["attendance"]
    )

    print("\n========================================")
    print("          STUDENT RESULT CARD")
    print("========================================")

    print("Student ID:", student["student_id"])
    print("Name:", student["name"])
    print("Class:", student["class_name"])
    print("Age:", student["age"])

    print("\nSubject Marks:")

    for subject in subjects:
        print(
            subject,
            ":",
            student["subjects"][subject]
        )

    print("\nTotal Marks:", int(total))
    print("Maximum Marks:", len(subjects) * 100)
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print("Result:", status)
    print("Attendance:", student["attendance"], "%")
    print("Attendance Status:", attendance_status)

    if average < 50 and student["attendance"] < 75:
        print(
            "Risk Status: Low Marks + Low Attendance"
        )

    elif average < 50:
        print("Risk Status: Low Marks")

    elif student["attendance"] < 75:
        print("Risk Status: Low Attendance")

    else:
        print("Risk Status: Safe")

    print("========================================")
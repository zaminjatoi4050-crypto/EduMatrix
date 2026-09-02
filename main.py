import numpy as np

from analytics import generate_analytics
from reports import display_student
from reports import generate_result
from storage import load_students
from storage import save_students
from validators import collect_marks
from validators import get_non_empty_text
from validators import get_valid_age
from validators import get_valid_percentage


print("**--**** Welcome to EduMatrix ****--**")


DATA_FILE = "students.json"


SUBJECTS = [
    "DS",
    "DSA",
    "QR II",
    "SRE",
    "SME",
    "Quran"
]


WEIGHTS = np.array([
    0.20,
    0.20,
    0.15,
    0.15,
    0.15,
    0.15
])


DEFAULT_STUDENTS = [
    {
        "student_id": "K25SW046",
        "name": "Engineer Jatoi",
        "class_name": "Lab 03",
        "age": 18,
        "subjects": {
            "DS": 85,
            "DSA": 80,
            "QR II": 78,
            "SRE": 88,
            "SME": 82,
            "Quran": 87
        },
        "attendance": 85,
        "previous_marks": {
            "DS": 90,
            "DSA": 78,
            "QR II": 98,
            "SRE": 67,
            "SME": 76,
            "Quran": 83
        }
    },
    {
        "student_id": "K25SW016",
        "name": "Abdul Wasiu",
        "class_name": "Lab 03",
        "age": 19,
        "subjects": {
            "DS": 85,
            "DSA": 80,
            "QR II": 78,
            "SRE": 88,
            "SME": 82,
            "Quran": 87
        },
        "attendance": 85,
        "previous_marks": {
            "DS": 95,
            "DSA": 70,
            "QR II": 68,
            "SRE": 98,
            "SME": 72,
            "Quran": 67
        }
    },
    {
        "student_id": "K25SW020",
        "name": "Sonia",
        "class_name": "3rd sem",
        "age": 18,
        "subjects": {
            "DS": 78,
            "DSA": 89,
            "QR II": 90,
            "SRE": 78,
            "SME": 89,
            "Quran": 90
        },
        "attendance": 89,
        "previous_marks": {
            "DS": 45,
            "DSA": 67,
            "QR II": 78,
            "SRE": 65,
            "SME": 67,
            "Quran": 78
        }
    }
]


STUDENTS = load_students(
    DATA_FILE,
    DEFAULT_STUDENTS
)


def save_current_data():
    saved = save_students(
        STUDENTS,
        DATA_FILE
    )

    if saved:
        print("Student data saved successfully.")


def find_student(student_id):
    for student in STUDENTS:
        if student["student_id"] == student_id:
            return student

    return None


def add_student():
    print("\n========== Add Student ==========")

    student_id = get_non_empty_text(
        "Enter Student ID: "
    )

    if find_student(student_id) is not None:
        print("This student ID already exists.")
        return

    student_name = get_non_empty_text(
        "Enter Student Name: "
    )

    class_name = get_non_empty_text(
        "Enter Student Class Name: "
    )

    age = get_valid_age()

    attendance = get_valid_percentage(
        "Enter Student Attendance: "
    )

    print("\nEnter Current Marks:")
    current_marks = collect_marks(SUBJECTS)

    print("\nEnter Previous Marks:")
    previous_marks = collect_marks(
        SUBJECTS,
        previous=True
    )

    new_student = {
        "student_id": student_id,
        "name": student_name,
        "class_name": class_name,
        "age": age,
        "subjects": current_marks,
        "attendance": attendance,
        "previous_marks": previous_marks
    }

    STUDENTS.append(new_student)
    save_current_data()

    print("Student added successfully.")


def view_all_students():
    if len(STUDENTS) == 0:
        print("No students found.")
        return

    print("\n========== All Students ==========")

    for student in STUDENTS:
        display_student(
            student,
            SUBJECTS
        )


def search_student():
    if len(STUDENTS) == 0:
        print("No students found.")
        return

    search_id = get_non_empty_text(
        "Enter Student ID to search: "
    )

    student = find_student(search_id)

    if student is None:
        print("Student not found.")
        return

    display_student(
        student,
        SUBJECTS
    )


def update_student():
    if len(STUDENTS) == 0:
        print("No students found.")
        return

    search_id = get_non_empty_text(
        "Enter Student ID to update: "
    )

    student = find_student(search_id)

    if student is None:
        print("Student not found.")
        return

    while True:
        print("\n========== Update Menu ==========")
        print("1. Update Name")
        print("2. Update Class")
        print("3. Update Age")
        print("4. Update Attendance")
        print("5. Update Current Marks")
        print("6. Update Previous Marks")
        print("7. Cancel")

        try:
            update_choice = int(
                input("Enter your update choice: ")
            )

            if update_choice == 1:
                student["name"] = get_non_empty_text(
                    "Enter new name: "
                )
                save_current_data()
                print("Name updated successfully.")
                return

            elif update_choice == 2:
                student["class_name"] = (
                    get_non_empty_text(
                        "Enter new class name: "
                    )
                )
                save_current_data()
                print("Class updated successfully.")
                return

            elif update_choice == 3:
                student["age"] = get_valid_age(
                    "Enter new age: "
                )
                save_current_data()
                print("Age updated successfully.")
                return

            elif update_choice == 4:
                student["attendance"] = (
                    get_valid_percentage(
                        "Enter new attendance: "
                    )
                )
                save_current_data()
                print("Attendance updated successfully.")
                return

            elif update_choice == 5:
                print("\nEnter new current marks:")
                student["subjects"] = collect_marks(
                    SUBJECTS
                )
                save_current_data()
                print(
                    "Current marks updated successfully."
                )
                return

            elif update_choice == 6:
                print("\nEnter new previous marks:")
                student["previous_marks"] = collect_marks(
                    SUBJECTS,
                    previous=True
                )
                save_current_data()
                print(
                    "Previous marks updated successfully."
                )
                return

            elif update_choice == 7:
                print("Update cancelled.")
                return

            else:
                print(
                    "Invalid choice. Please select 1 to 7."
                )

        except ValueError:
            print("Please enter a number only.")


def delete_student():
    if len(STUDENTS) == 0:
        print("No students found.")
        return

    search_id = get_non_empty_text(
        "Enter Student ID to delete: "
    )

    student = find_student(search_id)

    if student is None:
        print("Student not found.")
        return

    print("\n========== Student Details ==========")
    print("Student ID:", student["student_id"])
    print("Name:", student["name"])
    print("Class:", student["class_name"])
    print("Age:", student["age"])
    print("Attendance:", student["attendance"], "%")

    confirmation = input(
        "\nAre you sure you want to delete "
        "this student? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        STUDENTS.remove(student)
        save_current_data()
        print("Student deleted successfully.")

    else:
        print("Delete cancelled.")


def enter_marks():
    if len(STUDENTS) == 0:
        print("No students found.")
        return

    search_id = get_non_empty_text(
        "Enter Student ID to enter marks: "
    )

    student = find_student(search_id)

    if student is None:
        print("Student not found.")
        return

    print("\nCurrent Marks:")

    for subject in SUBJECTS:
        print(
            subject,
            ":",
            student["subjects"][subject]
        )

    print("\nEnter New Marks:")
    student["subjects"] = collect_marks(SUBJECTS)
    save_current_data()

    print("Marks updated successfully.")


def enter_attendance():
    if len(STUDENTS) == 0:
        print("No students found.")
        return

    search_id = get_non_empty_text(
        "Enter Student ID to enter attendance: "
    )

    student = find_student(search_id)

    if student is None:
        print("Student not found.")
        return

    print(
        "Current Attendance:",
        student["attendance"],
        "%"
    )

    new_attendance = get_valid_percentage(
        "Enter new attendance: "
    )

    student["attendance"] = new_attendance
    save_current_data()

    print("Attendance updated successfully.")


def generate_student_result():
    if len(STUDENTS) == 0:
        print("No students found.")
        return

    search_id = get_non_empty_text(
        "Enter Student ID to generate result: "
    )

    student = find_student(search_id)

    if student is None:
        print("Student not found.")
        return

    generate_result(
        student,
        SUBJECTS
    )


def main():
    while True:
        print("\n========== Main Menu ==========")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Enter Marks")
        print("7. Enter Attendance")
        print("8. Generate Result")
        print("9. Generate Analytics")
        print("10. Exit")

        try:
            choice = int(
                input("Enter your choice: ")
            )

            if choice == 1:
                add_student()

            elif choice == 2:
                view_all_students()

            elif choice == 3:
                search_student()

            elif choice == 4:
                update_student()

            elif choice == 5:
                delete_student()

            elif choice == 6:
                enter_marks()

            elif choice == 7:
                enter_attendance()

            elif choice == 8:
                generate_student_result()

            elif choice == 9:
                generate_analytics(
                    STUDENTS,
                    SUBJECTS,
                    WEIGHTS
                )

            elif choice == 10:
                save_current_data()
                print("Thank you for using EduMatrix.")
                break

            else:
                print(
                    "Invalid choice. Please select 1 to 10."
                )

        except ValueError:
            print(
                "Invalid input. Please enter a number."
            )


if __name__ == "__main__":
    main()
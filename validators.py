def get_non_empty_text(message):
    while True:
        value = input(message).strip()

        if value != "":
            return value

        print("This field cannot be empty.")


def get_valid_age(message="Enter Student Age: "):
    while True:
        try:
            age = int(input(message))

            if age > 0:
                return age

            print("Age must be a positive number.")

        except ValueError:
            print("Please enter age as a number.")


def get_valid_marks(subject_name):
    while True:
        try:
            marks = int(
                input(f"Enter {subject_name} marks: ")
            )

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter marks as a number.")


def get_valid_percentage(message):
    while True:
        try:
            percentage = int(input(message))

            if 0 <= percentage <= 100:
                return percentage

            print("Value must be between 0 and 100.")

        except ValueError:
            print("Please enter a number.")


def collect_marks(subjects, previous=False):
    marks = {}

    for subject in subjects:
        if previous:
            subject_name = "Previous " + subject
        else:
            subject_name = subject

        marks[subject] = get_valid_marks(subject_name)

    return marks
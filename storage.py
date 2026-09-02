import json
from copy import deepcopy


def save_students(students, filename="students.json"):
    try:
        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                students,
                file,
                indent=4,
                ensure_ascii=False
            )

        return True

    except OSError as error:
        print("Student data save nahi ho saka:", error)
        return False


def load_students(filename="students.json", default_students=None):
    if default_students is None:
        default_students = []

    try:
        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:
            saved_students = json.load(file)

        if isinstance(saved_students, list):
            return saved_students

        print(
            "students.json mein valid student list nahi hai."
        )
        return deepcopy(default_students)

    except FileNotFoundError:
        print(
            "students.json file nahi mili. "
            "Default data use hoga."
        )
        return deepcopy(default_students)

    except json.JSONDecodeError:
        print(
            "students.json corrupt hai. "
            "Default data use hoga."
        )
        return deepcopy(default_students)

    except OSError as error:
        print("Student data load nahi ho saka:", error)
        return deepcopy(default_students)
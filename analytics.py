import numpy as np

from reports import calculate_grade


def build_marks_matrix(students, subjects):
    marks_matrix = []

    for student in students:
        student_marks = []

        for subject in subjects:
            student_marks.append(
                student["subjects"][subject]
            )

        marks_matrix.append(student_marks)

    return np.array(
        marks_matrix,
        dtype=float
    )


def build_previous_marks_matrix(students, subjects):
    previous_matrix = []

    for student in students:
        student_marks = []

        for subject in subjects:
            student_marks.append(
                student["previous_marks"][subject]
            )

        previous_matrix.append(student_marks)

    return np.array(
        previous_matrix,
        dtype=float
    )


def generate_analytics(students, subjects, weights):
    if len(students) == 0:
        print("No students found.")
        return

    marks_matrix = build_marks_matrix(
        students,
        subjects
    )

    previous_matrix = build_previous_marks_matrix(
        students,
        subjects
    )

    student_totals = np.sum(
        marks_matrix,
        axis=1
    )

    student_averages = np.mean(
        marks_matrix,
        axis=1
    )

    subject_averages = np.mean(
        marks_matrix,
        axis=0
    )

    subject_medians = np.median(
        marks_matrix,
        axis=0
    )

    subject_maximums = np.max(
        marks_matrix,
        axis=0
    )

    subject_minimums = np.min(
        marks_matrix,
        axis=0
    )

    subject_standard_deviations = np.std(
        marks_matrix,
        axis=0
    )

    subject_variances = np.var(
        marks_matrix,
        axis=0
    )

    weighted_scores = np.dot(
        marks_matrix,
        weights
    )

    improvement_matrix = (
        marks_matrix - previous_matrix
    )

    student_improvements = np.sum(
        improvement_matrix,
        axis=1
    )

    class_average = np.mean(marks_matrix)

    highest_student_index = max(
        range(len(students)),
        key=lambda index: student_averages[index]
    )

    lowest_student_index = min(
        range(len(students)),
        key=lambda index: student_averages[index]
    )

    highest_improvement_index = max(
        range(len(students)),
        key=lambda index: student_improvements[index]
    )

    ranking_indices = sorted(
        range(len(students)),
        key=lambda index: weighted_scores[index],
        reverse=True
    )

    print("\n========================================")
    print("          CLASS ANALYTICS")
    print("========================================")

    print("Total Students:", len(students))
    print("Class Average:", round(class_average, 2))

    print(
        "Highest Student:",
        students[highest_student_index]["name"]
    )

    print(
        "Highest Average:",
        round(
            student_averages[highest_student_index],
            2
        )
    )

    print(
        "Lowest Student:",
        students[lowest_student_index]["name"]
    )

    print(
        "Lowest Average:",
        round(
            student_averages[lowest_student_index],
            2
        )
    )

    print("\nNumPy Matrix Information:")
    print("Shape:", marks_matrix.shape)
    print("Dimensions:", marks_matrix.ndim)
    print("Total Elements:", marks_matrix.size)
    print("Data Type:", marks_matrix.dtype)

    print("\nStudent-Wise Analytics:")

    for index, student in enumerate(students):
        print(
            student["name"],
            "| Total:",
            int(student_totals[index]),
            "| Average:",
            round(student_averages[index], 2),
            "| Weighted Score:",
            round(weighted_scores[index], 2)
        )

    print("\nSubject-Wise Analytics:")

    for index, subject in enumerate(subjects):
        print(
            subject,
            "| Average:",
            round(subject_averages[index], 2),
            "| Median:",
            round(subject_medians[index], 2),
            "| Maximum:",
            int(subject_maximums[index]),
            "| Minimum:",
            int(subject_minimums[index]),
            "| Standard Deviation:",
            round(
                subject_standard_deviations[index],
                2
            ),
            "| Variance:",
            round(
                subject_variances[index],
                2
            )
        )

    print("\n========== Student Ranking ==========")

    for rank, index in enumerate(
        ranking_indices,
        start=1
    ):
        print(
            rank,
            ".",
            students[index]["name"],
            "| Weighted Score:",
            round(weighted_scores[index], 2),
            "| Average:",
            round(student_averages[index], 2),
            "| Grade:",
            calculate_grade(
                student_averages[index]
            )
        )

    print("\n========== At-Risk Students ==========")

    risk_found = False

    for index, student in enumerate(students):
        reasons = []

        if student_averages[index] < 50:
            reasons.append("Low Marks")

        if student["attendance"] < 75:
            reasons.append("Low Attendance")

        if len(reasons) > 0:
            risk_found = True

            print(
                student["name"],
                "| Average:",
                round(student_averages[index], 2),
                "| Attendance:",
                student["attendance"],
                "%",
                "| Reason:",
                " + ".join(reasons)
            )

    if risk_found is False:
        print("No at-risk students found.")

    print("\n========== Improvement Report ==========")

    for index, student in enumerate(students):
        print(
            student["name"],
            "| Total Improvement:",
            int(student_improvements[index]),
            "| Average Improvement:",
            round(
                np.mean(improvement_matrix[index]),
                2
            )
        )

    print(
        "\nHighest Improvement:",
        students[highest_improvement_index]["name"]
    )

    print("========================================")
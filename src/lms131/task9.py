from to_do import TODO


def task9(grades):
    # grades is a list of dictionaries, where each dictionary has a student name and a list of their grades

    # Initialize total_grades to 0
    total_grades = 0

    # Iterate over the list of students
    for student in grades:
        # Get the student name and their grades
        name = student["name"]
        student_grades = student["grades"]

        # Calculate the total grade for the current student
        total_grade = 0
        for grade in student_grades:
            total_grade += grade

        # Add the total grade for the current student to the total_grades variable
        total_grades += total_grade

    # Calculate the average grade of the class
    result = total_grades / len(grades)

    print(result)

    return result


if __name__ == "__main__":
    task9({"Ana": [4.0, 4.5, 5.0],"John": [5.0, 5.0, 3.0],"Lise": [5.0, 5.0, 5.0]})

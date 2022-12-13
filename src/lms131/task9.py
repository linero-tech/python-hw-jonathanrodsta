from to_do import TODO


def task9(grades):
    # Create a variable to store the total number of grades
    total_grades = 0

    # Create a variable to store the sum of all the grades
    total_sum = 0

    # Check if the grades dictionary is empty
    if not grades:
        return 0.0

    # Loop through each student's grades
    for student, grades in grades.items():
        # Add the number of grades for this student to the total
        total_grades += len(grades)

        # Loop through each grade for this student
        for grade in grades:
            # Add the grade to the total sum
            total_sum += grade

    # Calculate the average grade
    result = total_sum / total_grades
    print(result)
    return result


if __name__ == "__main__":
    task9({"Ana": [4.0, 4.5, 5.0],"John": [5.0, 5.0, 3.0],"Lise": [5.0, 5.0, 5.0]})

from to_do import TODO


def task8(grades):
    result = ""
    highest_average = 0

    for student, grades in grades.items():
        # Calculate the average grade for the current student
        average_grade = 0
        for grade in grades:
            average_grade += grade
        average_grade /= len(grades)

        # Update the result if the current student has a higher average grade
        if average_grade > highest_average:
            result = student
            highest_average = average_grade

    print(result)

    return result

if __name__ == "__main__":
    task8()








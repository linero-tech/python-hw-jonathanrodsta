from to_do import TODO


def task8(grades):
    grades = [
        {"Ana": [4.0, 4.5, 5.0]},
        {"John": [5.0, 5.0, 3.0]},
        {"Lise": [5.0, 5.0, 5.0]},
    ]

    highest_average = 0
    result = ""

    for student_grades in grades:
        for student, grades in student_grades.items():

            total = 0
            for grade in grades:
                total += grade
            average = total / len(grades)


            if average > highest_average:
                highest_average = average
                result = student

    return result

if __name__ == "__main__":
    print(task8(" "))








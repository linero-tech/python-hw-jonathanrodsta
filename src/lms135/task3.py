from to_do import TODO


class Student:
    def __init__(self, grades: list):
        self._grades = grades

    @property
    def grades(self) -> list:
        return self._grades

    def gpa(self) -> float:
        return sum(self._grades) / len(self._grades)

    def bonus(self):
        self._grades = [grade + 1 for grade in self._grades]

    def lowest(self) -> float:
        return min(self._grades)

    def highest(self) -> float:
        return max(self._grades)


if __name__ == "__main__":
    # Create a student with grades [9, 7, 8, 10, 6]
    student = Student([1, 10, 5])

    # Calculate the GPA
    gpa = student.gpa()
    print(gpa)

    # Give the student a bonus by adding 1 point to each grade
    student.bonus()

    # Calculate the GPA again
    gpa = student.gpa()
    print(gpa)

    # Get the lowest grade
    lowest = student.lowest()
    print(lowest)

    # Get the highest grade
    highest = student.highest()
    print(highest)


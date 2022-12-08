from to_do import TODO

class Student:
    def __init__(self, grades: [float]):
        self.grades = grades

    @property
    def grades(self):
        return self.__grades

    def gpa(self):
        return sum(self.__grades) / len(self.__grades)

    def bonus(self):
        self.__grades = [grade + 1 for grade in self.__grades]

    def lowest(self):
        return min(self.__grades)

    def highest(self):
        return max(self.__grades)
if __name__ == "__main__":
    print()

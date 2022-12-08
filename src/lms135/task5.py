from to_do import TODO

import math


class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    def area(self) -> float:
        return math.pi * self._radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self._radius

if __name__ == "__main__":
    # Create a new Circle object with radius 5
    circle = Circle(5)

    # Calculate the area of the circle
    print(circle.area())  # 78.53981633974483

    # Calculate the perimeter of the circle
    print(circle.perimeter())  # 31.41592653589793



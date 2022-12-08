from to_do import TODO


class Rectangle:
    def __init__(self, base, height):
        self.__base = base
        self.__height = height

    def perimeter(self):
        return 2.0 * (self.__base + self.__height)

    def area(self):
        return self.__base * self.__height
if __name__ == "__main__":
    rect1 = Rectangle(base=1, height=1)
    print(rect1.perimeter())
    print(rect1.area())
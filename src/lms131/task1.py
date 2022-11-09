from to_do import TODO


def task1():
    result = dict()

    for number in range(10, 21):
        if number % 2 != 0:
            result[number] = number * 2

    return result




if __name__ == "__main__":
    print(task1())
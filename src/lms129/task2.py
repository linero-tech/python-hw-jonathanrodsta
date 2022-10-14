from to_do import TODO


def task2(number):
    result = 0

    for i in range(1, number + 1):
        if number % i == 0:
            result += 1

    result = result == 2

    return result


if __name__ == "__main__":
    task2(2)
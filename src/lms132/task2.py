from to_do import TODO


def task2(items):
    result = 0
    for item in items:

        if item is None:
            result += 1
    print(result)
    return result


if __name__ == "__main__":
    task2([1, None, 2, None, 3])

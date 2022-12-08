from to_do import TODO


def task2(items):
    result = items.count(None)
    if result == "":
        result = 0
        print(result)

    print(result)
    return result


if __name__ == "__main__":
    task2([1, None, 2, None, 3])

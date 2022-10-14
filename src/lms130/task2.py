from to_do import TODO


def task2(items):

    result = 0
    for index, number in enumerate(items):
        if index % 2 == 0:
            result += number
    print(result)

    return result









if __name__ == "__main__":
    task2([1,2,3,4])

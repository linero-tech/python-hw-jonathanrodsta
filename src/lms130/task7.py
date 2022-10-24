from to_do import TODO


def task7(items):
    result = 0
    if (len(items) != 0):

        result = items[0]
        for index in range(len(items)):

            if (items[index] > result):
                result = result
            else:
                result = items[index]
        print(result)
    else:
        result = 0
        print(result)
    return result


if __name__ == "__main__":
    task7([10,5,11])

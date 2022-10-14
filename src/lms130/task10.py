from to_do import TODO


def task10(items):

    even = 2
    odd = 3
    result = []

    for index in range(len(items)):

        if (items[index] % 2 == 0):
            result.append(items[index]*even)

        else:
            result.append(items[index]*odd)

    print(result)
    return result
if __name__ == "__main__":
    task10([1,2,3,4,5])

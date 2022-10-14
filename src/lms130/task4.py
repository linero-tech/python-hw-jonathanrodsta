from to_do import TODO


def task4(items, factor):
    result = []

    for i in items:
        if (i % factor == 0):
            result.append(i)

    print(result)
    return result




if __name__ == "__main__":
    task4([1,2,3,4,5,6],2)

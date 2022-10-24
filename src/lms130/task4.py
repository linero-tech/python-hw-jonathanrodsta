from to_do import TODO


def task4(items, factor):
    result = set()

    for number in items:
        if (number % factor == 0):
            result.add(number)

    print(result)
    return list (result)




if __name__ == "__main__":
    task4([1,2,3,4,5,6,],2)

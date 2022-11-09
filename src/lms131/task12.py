from to_do import TODO


def task12(a, b):
    result = dict()
    for index in range(len(a)):
        result[a[index]] = b[index]
    print(result)
    return result










if __name__ == "__main__":
    task12([1, 2, 3, 4],["W", "X", "Y", "Z"])
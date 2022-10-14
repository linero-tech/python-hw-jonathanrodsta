from to_do import TODO


def task3(items):
    x = items
    y = set(x)
    result = []
    for number in y :
        occurrences = x.count(number)
        if (occurrences > 1):
            result.append(number)
    print(result)
    return result





if __name__ == "__main__":
    task3([1,1,1,2,2,3])
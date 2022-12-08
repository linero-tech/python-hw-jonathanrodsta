from to_do import TODO


def task6(items):

    result = []
    if (items == ""):
        result = []

    for index, item in enumerate(items):
        if (items[index] == None):
            result.append(None)
        else:
            result.append(index * items[index])


    print(result)
    return result

if __name__ == "__main__":
    task6([0,2,None])

from to_do import TODO


def task9(items):
    result = items.copy()
    for index in range(len(items)):
        if (index == 0):
            temp = items[index]
            result[index] = temp * temp

        else:
            temp = items[index - 1]
            result[index] = result[index] * temp

    print(result)
    return result



if __name__ == "__main__":
    task9([5,2,3,4,])
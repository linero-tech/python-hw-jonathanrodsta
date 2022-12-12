from to_do import TODO


def task10(items):


    result = None
    for i in range(len(items)):
        if items[i] == "Nemo":
            result = i
            break

    print(result)  # should print 2
    return result


if __name__ == "__main__":
    task10(["I", "cannot","Nemo", "find", "him"])

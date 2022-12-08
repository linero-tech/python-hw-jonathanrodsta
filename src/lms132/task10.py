from to_do import TODO


def task10(items):
    result = None

    for index, element in enumerate(items):
        if element.lower() == "nemo":
            result = index
    print(result)
    return result





if __name__ == "__main__":
    task10(["I", "cannot","Nemo", "find", "him"])

from to_do import TODO


def task1(sentence):
    result = len(sentence)

    if sentence is None:
        result = 0
    else:
        result = len(sentence)

    print(result)
    return result


if __name__ == "__main__":
    task1("I love GBG")

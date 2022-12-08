from to_do import TODO


def task7(sentence):
    result = {}
    t = 0
    for i in sentence:
        if (i.isalpha()):
            t += 1
    result["letters"] = t
    result["digits"] = len(sentence) - t
    print(result)
    return result


if __name__ == "__main__":
    task7("H3ll0")


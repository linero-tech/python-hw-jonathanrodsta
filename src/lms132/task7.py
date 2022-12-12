from to_do import TODO


def task7(sentence):
    result = {"letters": 0, "digits": 0}
    for char in sentence:
        if char.isalpha():
            result["letters"] += 1
        elif char.isdigit():
            result["digits"] += 1

    print(result)

    return result


if __name__ == "__main__":
    task7("H3ll0")


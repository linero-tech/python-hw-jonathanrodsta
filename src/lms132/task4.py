from to_do import TODO


def task4(sentence):
    result = dict()

    if sentence is not None and sentence != "":
        result = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

        for character in sentence.lower():
            if character in result:
                result[character] += 1
    print(result)
    return result


if __name__ == "__main__":
    task4("Hello")

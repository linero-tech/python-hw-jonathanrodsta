from to_do import TODO


def task9(sentence, character):
    result = sentence.__contains__(character)
    print(result)
    return


if __name__ == "__main__":
    task9("I code in KOTLIN", "i")

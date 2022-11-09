from to_do import TODO


def task7(words):
    result = dict(zip(range(len(words)), words))

    print(result)
    return result


if __name__ == "__main__":
    task7(["I", "love", "Kotlin"])

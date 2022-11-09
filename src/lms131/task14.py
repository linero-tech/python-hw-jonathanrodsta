from to_do import TODO


def task14(sentence):
    sentence = sentence.lower()

    result = max(set(sentence), key=sentence.count)

    print(result)
    return result


if __name__ == "__main__":
    task14("I am it")

from to_do import TODO


def task1(sentence):
    result = len(sentence)

    print(result)

    sentence = "I love GBG"

    # Check if sentence is None
    if sentence is None:
        # If it is, then assign a value of 0 to result
        result = 0
    else:
        # Otherwise, calculate the length of the string
        result = len(sentence)

    # Print the result
    print(result)

    return result


if __name__ == "__main__":
    task1("I love GBG")

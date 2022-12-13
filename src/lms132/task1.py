from to_do import TODO


def task1(sentence):
    if sentence is None:
        result = 0
    else:
        result = len(sentence)


    
    return result


if __name__ == "__main__":
    sentence = "I love GBG"
    result = task1(sentence)

    print(result)  # Output: 10

    task1("I love GBG")

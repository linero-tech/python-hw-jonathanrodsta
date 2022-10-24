from to_do import TODO


def task6(sentence):
    result = ""

    for index, letter in enumerate(sentence):
        if index % 2 == 0:
            result += letter.upper()
        else:
            result += letter
    print(result)
    return result




if __name__ == "__main__":
    task6("I like Gothenburg")

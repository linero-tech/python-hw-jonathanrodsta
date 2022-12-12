from to_do import TODO


def task3(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if sentence == None:
        result = "*"
    else:
        result = sentence

        for letter in sentence:
            if letter.lower() in vowels:
                result = result.replace(letter, "*")
    return result


if __name__ == "__main__":
    print(task3("I live in SwEdEN"))

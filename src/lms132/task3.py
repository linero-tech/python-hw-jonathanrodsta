from to_do import TODO


def task3(sentence):
    vowels = ('a', 'e', 'i', 'o', 'u')
    result = "*"
    for character in sentence:
        if character.lower() in vowels:
            sentence = sentence.replace(character, result)
    return sentence


if __name__ == "__main__":
    print(task3("I live in SwEdEn"))

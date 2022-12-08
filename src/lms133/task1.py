from to_do import TODO


def remover(sentence):
    result = ""
    vowels = ["a", "e", "i", "o", "u"]

    for letter in sentence:
        if letter.lower() not in vowels:
            result += letter



    return result
if __name__ == "__main__":
    print(remover("Sweden is nice"))

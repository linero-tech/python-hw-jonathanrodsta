from to_do import TODO


def task13(sentence):

    word_count = {}

    words = sentence.split(" ")

    for word in words:

        word = word.replace(",", "").replace(";", "").replace(".", "").replace(":", "")

        word = word.lower()

        if word in word_count:

            word_count[word] += 1
        else:

            word_count[word] = 1

    result = words[0]

    for word, count in word_count.items():
        if count > word_count[result]:
            result = word

    print(result)
    return result


if __name__ == "__main__":
    task13("this This THIS is still the very very same")

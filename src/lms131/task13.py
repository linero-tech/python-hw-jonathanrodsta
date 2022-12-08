from to_do import TODO


def task13(sentence):
    sentence = sentence.lower()
    words = sentence.split(" ")
    dict = {}


    for word in words:
        word = word.replace(",", "").replace(";", "").replace(".", "").replace(":", "")
        dict[word] = words.count(word)
    result = max(dict, key=dict.get)
    print(result)
    return result




if __name__ == "__main__":
    task13("this This THIS is still the very very same")

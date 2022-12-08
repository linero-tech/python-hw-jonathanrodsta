from to_do import TODO


def task5(word):
    if word == "":
        return False
    if word == None:
        return False
    clean_word = word.lower()
    result = []
    for letter in clean_word:
        if letter.isalpha():
            if letter in result:
                return False
            result.append(letter)
    return True

if __name__ == "__main__":
    print(task5("space"))


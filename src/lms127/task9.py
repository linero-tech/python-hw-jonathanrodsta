from to_do import TODO


def task9(sentence, character):
    lower_sentence = sentence.lower()
    lower_character = character.lower()
    result = lower_character in lower_sentence
    print(result)
    return result


if __name__ == "__main__":
    task9("I code In KOTLIN", "i")

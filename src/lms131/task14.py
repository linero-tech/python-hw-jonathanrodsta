from to_do import TODO
import re


def task14(sentence):
    character_count = dict()

    for character in re.sub(r' ', "", sentence.lower()):
        if character in character_count:
            character_count[character] = character_count[character] + 1
        else:
            character_count[character] = 1

    result = max(character_count, key=character_count.get)

    return result


if __name__ == "__main__":
    print(task14("I am it"))

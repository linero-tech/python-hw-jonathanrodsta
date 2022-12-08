from to_do import TODO

import string as STR


def counter(sting):
    result = False
    position_total = 1
    alphabet_dict = {letter: index for index, letter in enumerate(list(STR.ascii_lowercase))}

    if sting is not None:
        for character in sting.lower().replace(" ",""):
            if character in alphabet_dict:
                position_total += alphabet_dict.get(character)
    if position_total != 0 and position_total % 2 == 0:
        result = True
    return result


if __name__ == "__main__":
    print(counter("alexa"))

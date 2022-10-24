import re

from to_do import TODO


def task10(password):
    pattern1 = "[a-z]"
    pattern2 = "[A-Z]"
    pattern3 = "[0-9]"
    pattern4 = "[$#@]"

    has_lowercase = re.findall(pattern1,password)
    has_uppercase = re.findall(pattern2,password)
    has_number = re.findall(pattern3, password)
    has_special_character = re.findall(pattern4, password)
    has_correct_length = len(password) in range(6,11)

    result = has_lowercase and has_uppercase and has_number and has_special_character and has_correct_length
    return result

if __name__ == "__main__":
    print(task10("Hejsan@1"))



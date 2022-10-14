import random

from to_do import TODO


def task1(items):
    is_list_empty = len(items) == 0

    if is_list_empty:
        result = 0
    else:
        start_index = 0
        last_index = len(items) - 1

        random_index = random.randint(start_index, last_index)

        result = items[random_index]

    return result

if __name__ == "__main__":
    print(task1([6,12,60,100]))

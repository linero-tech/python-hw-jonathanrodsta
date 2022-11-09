from to_do import TODO


def task2(mapa):
    result = 0

    for key, value in mapa.items():
        result += key

    return result




if __name__ == "__main__":
    print(task2({1: 10, 2: 20, 3: 30}))

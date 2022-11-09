def task10(mapa):
    result = dict()

    for key, value in mapa.items():
        result[value] = key

    return result


if __name__ == "__main__":
    print(task10({1: "A", 2: "B", 3: "C"}))


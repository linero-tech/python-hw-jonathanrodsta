from to_do import TODO


def task4(mapa, value):
    result = []
    for key, mapa_value in mapa.items():
        if value == mapa_value:
            result.append(key)
    print(result)
    return result


if __name__ == "__main__":
    task4({1: 100, 2: 100, 3: 200}, 100)

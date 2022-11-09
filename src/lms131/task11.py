from to_do import TODO


def task11(mapa, prospect):
    result = False
    for key, value in mapa.items():
        if key == prospect:
            result = True
            break

    print(result)
    return result


if __name__ == "__main__":
    task11({1: "A", 2: "B", 3: "C"}, 1)

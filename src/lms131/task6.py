from to_do import TODO


def task6(mapa, parameter):
    result = {}

    for key, value in mapa.items():
        if value == parameter:
            result[key] = parameter
    print(result)
    return result


if __name__ == "__main__":
    task6({20: "Ana", 40: "John", 22: "Ana"}, "Ana")

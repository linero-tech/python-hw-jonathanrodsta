from to_do import TODO


def task5(mapa, constant):
    result = []
    for key, mapa_value in mapa.items():
        if constant != mapa_value:
            result.append(key)
    print(result)
    return result

if __name__ == "__main__":
    task5({1: 100, 3: 200, 4: 500}, 100)


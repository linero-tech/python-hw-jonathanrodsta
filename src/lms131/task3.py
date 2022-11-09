from to_do import TODO


def task3(a, b):
    result = []
    for (ak, av), (bk, bv) in zip(a.items(), b.items()):
        if ak == bk:
            result.append(ak)

    print(result)

    return result


if __name__ == "__main__":
    task3({1: "A", 2: "B", 3: "C"}, {1: "A", 2: "B", 4: "D"})

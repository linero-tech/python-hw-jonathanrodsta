from to_do import TODO


def task8(items):
    result = []

    for i in items:
        if i is not None and len(i) > 3:
            result.append(i)
    print(result)
    return result


if __name__ == "__main__":
    task8(["Hello", "Gothenburg",None])

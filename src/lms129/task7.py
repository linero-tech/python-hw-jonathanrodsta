from to_do import TODO


def task7(a, b):

    result = 1
    for b in range(b, 0, -1):
        result *= a
    print(result)
    return (result)

if __name__ == "__main__":
    task7(2,3)

from to_do import TODO


def task9(identification):
    result = False

    if identification is not None:
        year = int(identification[0:4])
        month = int(identification[4:6])
        day = int(identification[6:8])

        if year >= 1947 and month in range(1, 13) and day in range(1, 32) and len(identification) == 13:
            result = True
    return result


if __name__ == "__main__":
    print(task9("19921117-9078"))
    print(task9(None))
    print(task9("19470110-1739"))

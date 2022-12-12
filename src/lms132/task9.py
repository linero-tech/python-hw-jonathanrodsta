from to_do import TODO


def task9(identification):
    result = False

    if identification is not None:
        year = int(identification[0:4])
        month = int(identification[4:6])
        day = int(identification[6:8])

        if year >= 1947 and (1 <= month <= 12) and (1 <= day <= 31) and len(identification):
            result = True

    return result


if __name__ == "__main__":
    print(task9("19921117-9078"))
    print(task9(None))

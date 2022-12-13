from to_do import TODO


def task9(identification):
    result = False

    if identification is None:
        result = False
    else:
        try:
            year = int(identification[0:4])
            month = int(identification[4:6])
            day = int(identification[6:8])

            if year >= 1947 and (1 <= month <= 12) and (1 <= day <= 31) and len(identification) == 13:
                result = True
        except ValueError as ve:
            result = False
    return result


if __name__ == "__main__":
    print(task9("19922331-1090"))  # wrong month False
    print(task9(None))  # False
    print(task9("19200112-1090"))  # wrong year False
    print(task9("1992-3131-1090"))  # False wrong PN
    print(task9('19920189-1090'))  # wrong day False
    print(task9("19921117-9078"))  # True

from to_do import TODO


def task9(identification):
    if identification is None:
        result = False
    elif len(identification) != 13:
        result = False
    else:
        year = identification[0:4]
        if not year.isdigit() or identification[4] != '-' or not identification[5:8].isdigit():
            result = False
        else:
            year = int(year)
            if year < 1947:
                result = False
            else:
                result = True
    return result


if __name__ == "__main__":
    print(task9("19921117-9078"))
    print(task9(None))
    print(task9("19470110-1739"))
    print(task9("19923131-1090"))

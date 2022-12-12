from to_do import TODO


def task8(number):

    result = 0

    for i in str(number):
        result += int(i)

    print(result)
    return result



if __name__ == "__main__":
    task8(123)
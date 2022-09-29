from to_do import TODO


def task6(number):
    result = number
    rev = 0


    while (result > 0):
        a = result % 10
        rev = rev * 10 + a
        result = result // 10
        print(rev)

    return (result)



if __name__ == "__main__":
    task6(678)
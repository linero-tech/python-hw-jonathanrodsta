from to_do import TODO


def task3(number):
    result = 1
    for i in range(number-1):
        result *= number-i

    return (result)



if __name__ == "__main__":
    x = task3(5)
    print(x)

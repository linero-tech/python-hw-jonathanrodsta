from to_do import TODO


def task1(a, b):

    result = 0
    boolCheck = False
    for a in range(a, b + 1):
        if  a >= b:
            if (boolCheck):
                result += a
            else:
                result = 0
                break
        else:
            boolCheck = True
            result += a

    print(result)
    return (result)

if __name__ == "__main__":
    task1 (1,5)
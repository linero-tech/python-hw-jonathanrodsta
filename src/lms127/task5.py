from to_do import TODO


def task5(value_for_a, value_for_b):
    a = value_for_a
    b = value_for_b
    temp = a
    a = b
    b = temp

    # result = a, b = b, a
    print(a,b)
    return a, b

if __name__ == "__main__":
    task5(1,2)

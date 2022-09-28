from to_do import TODO


def task2(number):
    result = False
    if number > 1:
        # check for factors
        for i in range(2, number):
            if (number % i) == 0:
                # if factor is found, set result to True
                result = True
                # break out of loop
                break

    # check if result is True
    if result:
        print(number, "is not a prime number")
    else:
        print(number, "is a prime number")
    return (result)


if __name__ == "__main__":
    task2(5)
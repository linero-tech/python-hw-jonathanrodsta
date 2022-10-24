from to_do import TODO


def task6(number):
    result = 0
    if (number % 10 == 0):
        print(number, " is divisble by 10 sorry! ")
    else:
        tempStr = str(number)

        temp = tempStr[::-1]

        tempNum = int(temp)
        tempInt = int(temp)
        while tempInt > 0:
            if (tempInt == tempNum):
                result = tempInt
            tempInt = tempInt - 1
    print(result)

    return result



if __name__ == "__main__":
    task6(678)
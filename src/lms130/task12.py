from to_do import TODO


def task12_1(sells):
    HighestSells = max(sells)
    index = sells.index(HighestSells)
    if (index == 0):
        result = "Monday"
    elif (index == 1):
        result = "Tuesday"
    elif (index == 2):
        result = "Wednesday"
    elif (index == 3):
        result = "Thursday"
    elif (index == 4):
        result = "Friday"
    elif (index == 5):
        result = "Saturday"
    elif (index == 6):
        result = "Sunday"

    print(result)
    return result




if __name__ == "__main__":
    task12_1([20, 100, 800, 768, 765, 90, 10])

def task12_2(sells):
    Least_sells = min(sells)
    index = sells.index(Least_sells)
    if (index == 0):
        result = "Monday"
    elif (index == 1):
        result = "Tuesday"
    elif (index == 2):
        result = "Wednesday"
    elif (index == 3):
        result = "Thursday"
    elif (index == 4):
        result = "Friday"
    elif (index == 5):
        result = "Saturday"
    elif (index == 6):
        result = "Sunday"

    print(result)
    return result



if __name__ == "__main__":
    task12_2([20, 100, 800, 768, 765, 90, 10])


def task12_3(sells):
    result = sum(sells)

    print(result)
    return result




if __name__ == "__main__":
    task12_3([20, 100, 800, 768, 765, 90, 10])


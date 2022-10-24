from to_do import TODO


def task4():
    number = 9
    result = 0
    sum = 0
    for number in range(number, 1000):
        if (number % 9 == 0):
            sum = sum + number
            result = sum
            
    print(result)
    return result



if __name__ == "__main__":
    task4()

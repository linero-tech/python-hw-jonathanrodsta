from to_do import TODO


def task8(number):


    numStr = str(number)
    list_of_num = list(map(int, numStr.strip()))
    result = sum(list_of_num)

    print(result)
    return(result)



if __name__ == "__main__":
    task8(213)
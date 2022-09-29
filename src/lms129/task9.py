from to_do import TODO


def task9(temperature):
    result = 0
    if (temperature.find("c") != -1):
        tempCel = temperature.replace("c", "")
        tempFloat = float(tempCel)
        tempResult = (tempFloat * 9/5) + 32
        tempResult = int(tempResult)
        result = str(tempResult)
        result = result + "f"
        result = result.strip()


    elif (temperature.find("C") != -1):
        tempCel = temperature.replace("C", "")
        tempFloat = float(tempCel)
        tempResult = (tempFloat * 9/5) + 32
        tempResult = int(tempResult)
        result = str(tempResult)
        result = result + "F"
        result = result.strip()


    elif (temperature.find("f") != -1):
        tempFahr = temperature.replace("f", "")
        tempFloat = float(tempFahr)
        tempResult = (tempFloat - 32) * 5/9
        tempResult = int(tempResult)
        result = str(tempResult)
        result = result + "c"
        result = result.strip()


    elif (temperature.find("F") != -1):
        tempFahr = temperature.replace("F", "")
        tempFloat = float(tempFahr)
        tempResult = (tempFloat - 32) * 5/9
        tempResult = int(tempResult)
        result = str(tempResult)
        result = result + "C"
        result = result.strip()


    else:
        print("did not find correct character!")

    print(result)

    return result
if __name__ == "__main__":
    task9("-30c")
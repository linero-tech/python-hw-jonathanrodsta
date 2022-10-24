from to_do import TODO


def task9(temperature):
    result = 0
    if temperature[-1] == "C" or temperature[-1] == "c":
        result= (int(temperature[0:-1]) * 9/5) + 32
        result = str(int(result)) + "F"
    elif temperature[-1] == "F" or temperature[-1] == "f":
        result = (int(temperature[0:-1]) - 32) * 5/9
        result = str(int(result)) + "C"
        print(result)
        return result
if __name__ == "__main__":
    task9("50F")
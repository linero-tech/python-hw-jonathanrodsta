from to_do import TODO


def task10_1(assessments):

    result = len(assessments)
    print(result)
    return result




def task10_2(assessments):
    result = assessments[3]
    print(result)
    return result





def task10_3(assessments):
    number_of_assessments = len(assessments)
    index_of_middle_assessments = int(number_of_assessments/2)
    result = assessments[index_of_middle_assessments]
    print(result)
    return result






def task10_4(assessments):
    result = assessments[0:3]
    print(result)
    return result


if __name__ == "__main__":
    task10_1("LMHHF")
    task10_2("LMFHMF")
    task10_3("LMFHM")
    task10_4("LMFHM")




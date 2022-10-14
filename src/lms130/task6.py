from to_do import TODO


def task6(sentence):
    temp = []
    result = ""
    for index in range(len(sentence)):
        if index % 2 == 0:
            temp.append(sentence[index].upper())
        else:
            temp.append(sentence[index])
    result = ' '.join(temp)
    print(result)
    return result




if __name__ == "__main__":
    task6("I like Gothenburg")

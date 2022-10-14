from to_do import TODO


def task5(items):
    result = []
    counter = 0
    for i in items:
        result.append(i * counter)
        counter = counter + 1
    print(result)
    return result



if __name__ == "__main__":
    task5([1,5,11])

from to_do import TODO


def task8(items):
    num = sorted([(x, i) for (i, x) in enumerate(items)], reverse=True)
    result = []
    for x, i in num:
        if i & x not in result:
            result.append(x)
            if len(result) == 3:
                break

    print(result)
    return result



if __name__ == "__main__":
    task8([60,9,7,10,1222,111,33])

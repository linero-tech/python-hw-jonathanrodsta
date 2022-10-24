from to_do import TODO


def task8(items):
    #num = sorted([(x, i) for (i, x) in enumerate(items)], reverse=True)
    #result = []
    #for x, i in num:
        #if i & x not in result:
            #result.append(x)
            #if len(result) == 3:
                #break
    items_as_set = set(items)
    it = list(items_as_set)
    it.sort()


    return it[-3:]



if __name__ == "__main__":
    print(task8([60,9,7,10]))

from to_do import TODO

def censorship(text):
    result = []
    for word in text.split(" "):
        if len(word) > 4:
            result.append("*" * len(word))
        else:
            result.append(word)
    return " ".join(result)






if __name__ == "__main__":
    print(censorship("I live in Sweden"))

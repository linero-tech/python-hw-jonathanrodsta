from to_do import TODO


def vowels(string):
    count = 0
    string = string.lower()
    for letter in string:
        if (letter == "a"):
            count += 5
        elif(letter == "e"):
            count += 4
        elif(letter == "i"):
            count += 3
        elif(letter == "o"):
            count += 2
        elif(letter == "u"):
            count += 1
    return count



if __name__ == "__main__":
    print(vowels("I love kotlin"))

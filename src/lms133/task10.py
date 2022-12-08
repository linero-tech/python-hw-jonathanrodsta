from to_do import TODO


def tweet(message: str) -> str:
    # get   the length of text
    # number of @ symbol needed = 280 - length
    # multiple the "@" symbol * the amount we need result.append("*" * len(word))
    # append to the end of the sentence the result from previous step
    remaining_chars = 280 - len(message)

    filler = "@" * remaining_chars

    return message + filler


if __name__ == "__main__":
    print(tweet("I feel good today!"))

from to_do import TODO


def task7(sentence):
    # Initialize the counts
    letters = 0
    digits = 0

    # Check if sentence is not null
    if sentence is not None:
        # Iterate over each character in sentence
        for char in sentence:
            # Check if the character is a letter
            if char.isalpha():
                letters += 1
            # Check if the character is a digit
            elif char.isdigit():
                digits += 1

    # Save the counts in result
    result = {
        "letters": letters,
        "digits": digits
    }
    print(result)

    return result


if __name__ == "__main__":
    task7(None)


from to_do import TODO


def task15(sentence):
    # Create an empty dictionary to store the counts
    result = {}

    # Split the sentence into a list of words
    words = sentence.split()

    # Loop through each word in the list of words
    for word in words:
        # Get the first letter of the word, in lowercase
        first_letter = word[0].lower()

        # If the letter is not in the dictionary, add it and set the count to 1
        if first_letter not in result:
            result[first_letter] = 1

        # Otherwise, increment the count for that letter
        else:
            result[first_letter] += 1

    # Print the result
    print(result)
    return result
if __name__ == "__main__":
    task15("This is the Very small Text")



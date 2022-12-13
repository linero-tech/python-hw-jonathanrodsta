from to_do import TODO


def task3(sentence):
    # Initialize an empty string to store the modified sentence
    modified_sentence = ""

    # Check if sentence is not null
    if sentence is not None:
        # Iterate over each character in sentence
        for char in sentence:
            # Check if the character is a vowel
            if char.lower() in "aeiou":
                # Replace the character with an asterisk (*)
                modified_sentence += "*"
            else:
                # Otherwise, keep the character as is
                modified_sentence += char

    # Return the modified sentence
    return modified_sentence


if __name__ == "__main__":
    print(task3("I live in SwEdEn"))

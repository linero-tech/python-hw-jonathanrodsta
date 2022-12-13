from to_do import TODO


def task13(sentence):
    # Split the sentence into words and remove special characters
    words = sentence.split()
    for i, word in enumerate(words):
        words[i] = word.strip(".,:;").lower()

    # Count the frequency of each word
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Find the word with the highest frequency
    max_count = 0
    max_word = ""
    for word, count in word_counts.items():
        if count > max_count:
            max_count = count
            max_word = word

    # Save the result in lowercase
    result = max_word.lower()

    print(result)
    return result


if __name__ == "__main__":
    task13('this, This; THIS, is still the very very same')

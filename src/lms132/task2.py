from to_do import TODO


def task2(items):
    # Initialize the counter variable to 0
    result = 0

    # Iterate over the items list
    for item in items:
        # Check if the current element is null
        if item == None:
            # Increment the counter variable
            result += 1

    # Print the result
    print(result)

    return result


if __name__ == "__main__":
    task2([1, None, 2, None, 3])

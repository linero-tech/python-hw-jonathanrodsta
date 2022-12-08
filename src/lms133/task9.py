from to_do import TODO

def harshad(number):
    if number == 0:
        return False

    num = number
    sum_of_digits = 0

    while num != 0:
        last_digit = num % 10

        sum_of_digits += last_digit

        num = int(num / 10)

    return number % sum_of_digits == 0




if __name__ == "__main__":
    print(harshad(1))



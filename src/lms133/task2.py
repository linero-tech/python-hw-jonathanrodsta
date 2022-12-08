from to_do import TODO


def fizzBuzzFoo(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"

    elif number % 5 == 0:

        return "Buzz"

    elif number % 3 == 0:
        return "Fizz"
    else:
        return "Foo"


if __name__ == "__main__":
    print(fizzBuzzFoo(5))

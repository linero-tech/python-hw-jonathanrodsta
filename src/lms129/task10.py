from to_do import TODO


def task10(password):

    global len
    checkpoint = False
    specialCharacter = ["$", "#", "@"]
    result = len(password)
    print(password)
    lenghtCheck = False
    UpperAndLowerCheck = False
    DigitCheck = False
    SpecialCharacterCheck = False

    print(len)

    # check length

    if (result >= 6 and result <= 10):
        print("this password has enough characters")
        checkpoint = True
        lenghtCheck = True
    else:
        checkpoint = False
        print("This password does not have enough characters")
        checkpoint = False

        # upper and lower
    if (password.islower() == False and password.isupper() == False):
        print("This password contains both upper and lower")
        UpperAndLowerCheck = True
        checkpoint = True

    else:
        print("The password does not have lowercase and uppercase!")

    # Digit check
    for len in password:
        if len.isdigit():
            checkpoint = True
            DigitCheck = True
            print("This password contains one digit or more")
            break
        else:
            checkpoint = False
    if (checkpoint == False):
        print("You must include a digit in password 0-9")
        checkpoint = False

        # special character!
    if any(c in specialCharacter for c in password):
            checkpoint = True
            SpecialCharacterCheck = True
            print("this password contains one or more of the special characters!",
                  specialCharacter)

    else:
            checkpoint = False
            print("Your password must contain these characters:", specialCharacter)

    if (lenghtCheck == True and UpperAndLowerCheck == True and DigitCheck == True
                and SpecialCharacterCheck == True):
            result = password
            print(result, "This is a good password")
            return result

    else:
            print("Incorrect Password")
            incorrectPass = password
            return incorrectPass

if __name__ == "__main__":
    task10("Hejsan2#")



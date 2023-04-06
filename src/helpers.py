# helpers.py
# Contains misc helper functions

import string
import random


# Generate a random string of given length
def rndString(length):
    letters = string.ascii_letters
    result = ''.join(random.choice(letters) for i in range(length))
    return result


# Get integer input with verification
def getIntInp(min, max):
    while True:
        try:
            inputInteger = input()
            if inputInteger == "":
                break
            if inputInteger.isdigit():
                inputInteger = int(inputInteger)
            else:
                raise ValueError()
            if (min <= int(inputInteger) <= max):
                break
            raise ValueError()

        except ValueError:
            print("Error: Incorrect input, please try again!\n")

    return inputInteger


# Get yes/no (boolean) input with verification
def getYesNoInp():
    while True:
        try:
            inputBool = input()
            if inputBool == "" or inputBool.lower() == "yes" or inputBool.lower() == "no":
                break
            else:
                raise ValueError()

        except ValueError:
            print("Error: Incorrect input, please try again!\n")

    if inputBool.lower() == "yes":
        return True
    else:
        return False

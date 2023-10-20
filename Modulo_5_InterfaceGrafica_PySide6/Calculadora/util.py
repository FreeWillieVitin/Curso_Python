import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def inNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))


def validNumber(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid


def isEmpty(string: str):
    return len(string) == 0


def convertNumber(string: str):
    Number = float(string)

    if Number.is_integer():
        Number = int(Number)

    return Number

# print(NUM_OR_DOT_REGEX.search('9'))

def getExponential(a, b):
    return a ** b


def testGreaterThan10(x):
    return None if x == 10 else x > 10


def getSquared(numbers):
    if not isinstance(numbers, list):
        raise ValueError('Only accepts a list!')
    return [getExponential(x, 2) for x in numbers]


if __name__ == '__main__':
    print(getSquared([1, 2, 3]))
    print(testGreaterThan10(5))
    print(getExponential(2, 3))

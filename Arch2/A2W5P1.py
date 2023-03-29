import random


def summation():
    corr, incorr = 0, 0
    for i in range(10):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        answer = input(f'{a} + {b} = ')
        if answer == a + b:
            corr += 1
        else:
            incorr += 1
    return [corr, incorr]


def subtraction():
    corr, incorr = 0, 0
    for i in range(10):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        answer = input(f'{a} - {b} = ')
        if answer == a - b:
            corr += 1
        else:
            incorr += 1
    return [corr, incorr]


def multiplication():
    corr, incorr = 0, 0
    for i in range(10):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        answer = input(f'{a} * {b} = ')
        if answer == a * b:
            corr += 1
        else:
            incorr += 1
    return [corr, incorr]


def arithmetic_operation(arithmetic_type):
    if arithmetic_type.lower() == "summation":
        a = summation()
    elif arithmetic_type.lower() == "subtraction":
        a = subtraction()
    elif arithmetic_type.lower() == "multiplication":
        a = multiplication()
    print(a)

if __name__ == "__main__":
    arithmetic_type = input()
    arithmetic_operation(arithmetic_type)
def btd(b):
    b = str(b)
    ml = []
    a = len(b) - 1
    while a > 0:
        b = str(b)
        a = len(b) - 1
        n = 10 ** a
        b = int(b)
        if n <= b:
            b -= n
            ml.append(a)
        else:
            if b != 0:
                continue
            else:
                a = 0
    s = 0
    for i in ml:
        s += 2 ** i
    print(s)


if __name__ == "__main__":
    b = input()
    btd(b)
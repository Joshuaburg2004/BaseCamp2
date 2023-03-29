def and_():
    print("AND")
    s = True and True
    t = False and True
    u = True and False
    v = False and False
    print('True + True =', s)
    print('False + True =', t)
    print('True + False =', u)
    print('False + False =', v)
    print("")


def or_():
    print("OR")
    s = True or True
    t = False or True
    u = True or False
    v = False or False
    print('True + True =', s)
    print('False + True =', t)
    print('True + False =', u)
    print('False + False =', v)


if __name__ == "__main__":
    and_()
    or_()
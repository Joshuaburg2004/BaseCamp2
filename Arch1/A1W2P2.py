def leap(y):
    y = int(y)
    leap = False
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap


if __name__ == "__main__":
    y = input()
    e = leap(y)
    if e is True:
        print(f"{y} is a Leap year!")
    else:
        print(f"{y} is not a Leap year!")
def htdy(y):
    y = int(y)
    if y < 0:
        print("Only possitive numbers are allowed")
    else:
        #2-y, not y-2!
        if 2 - y >= 0:
            dy = y * 10.5
        else:
            dy = 2 * 10.5 + (y - 2) * 4
    dy = str(dy)
    return dy


if __name__ == "__main__":
    y = input()
    dy = htdy(y)
    print(f"Dog years: {dy}")
def int_converter(i):
    try:
        i = int(i)
    except ValueError:
        print("ERROR: Please input a number")
    return i


def w_g(g):
    g = int_converter(g)
    wg = g * 112
    return wg


def w_w(w):
    w = int_converter(w)
    ww = w * 75
    return ww


if __name__ == "__main__":
    w = input("Please input how many widgets are you ordering: ")
    ww = w_w(w)
    g = input("Please input how many gizmo's are you ordering: ")
    wg = w_g(g)
    total = str(ww + wg)
    print(f"The Total Weight of the Order: {total} grams")
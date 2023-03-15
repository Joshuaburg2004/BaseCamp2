def taxandtipcalc():
    p = input()
    try:
        p = float(p)
    except ValueError:
        print("Please input a number")
    return p


if __name__ == "__main__":
    p = taxandtipcalc()
    tip = 0.15 * p
    tax = 0.21 * p
    total = p + tip + tax
    print("Tax: " + str(format(tax, '.3f')) + ", Tip: " + str(format(tip, '.3f')) + ", Total: " + str(format(total, '.3f')))
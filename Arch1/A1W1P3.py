def float_convert(n):
    try:
        n = float(n)
    except ValueError:
        print("ERROR: Please input a number")
    return n


if __name__ == "__main__":
    height = input("Please give a height: ")
    height = float_convert(height)
    width = input("Please give a width: ")
    width = float_convert(width)
    area = height * width
    area = str(area)
    print(f"Area: {area}")
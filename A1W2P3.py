def shape(n):
    n = int(n) - 3
    my_list = ['Triangle',
    'Square',
    'Pentagon',
    'Hexagon',
    'Heptagon',
    'Octagon',
    'Nonagon',
    'Decagon']
    if n >= 0 and n < len(my_list):
        shape = my_list[n]
        return shape
    else:
        print("Index out of range.")


if __name__ == "__main__":
    n = input()
    a = shape(n)
    print(a)
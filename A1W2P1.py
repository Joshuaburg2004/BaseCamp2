def eoo(a):
    even = "even"
    odd = "odd"
    if a.isdigit():
        if int(a) % 2 == 0:
            return even
        else:
            return odd
    else:
        print("ERROR")


if __name__ == "__main__":
    e = input()
    a = eoo(e)
    print(a)
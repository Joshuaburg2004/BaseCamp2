def mod_rectangle(w, h):
    w = int(w)
    h = int(h)
    p = 0
    for j in range(0, h):
        for i in range(0, w):
            if i < w - 1:
                print(p % 10, end=' ')
            elif i == w - 1:
                print(p % 10, end='\n')
            p += 1


if __name__ == "__main__":
    w = input("Width: ")
    h = input("Height: ")
    mod_rectangle(w, h)
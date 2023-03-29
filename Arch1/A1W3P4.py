def ctf():
    c = 0
    print("°C °F")
    for i in range(0, 10):
        c += 10
        f = (9 / 5) * c + 32
        f = int(f)
        f = str(f)
        print(f"{c} {f}")


if __name__ == "__main__":
    ctf()        
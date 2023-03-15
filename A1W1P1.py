def get_name():
    n = input("Please input your name: ")
    return n


if __name__ == "__main__":
    n = get_name()
    print(f"Hello {n}!")
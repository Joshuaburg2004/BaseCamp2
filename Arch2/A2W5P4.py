def is_integer(unchecked: str):
    try:
        int(unchecked)
        print("valid")
        return True
    except ValueError:
        print("invalid")
        return False


def remove_non_integer(unchecked: str):
    a = 0
    my_list = []
    for char in unchecked:
        a += 1
        if a == 1:
            if char.isdigit() or char == '-':
                if char == '0':
                    pass
                else:
                    my_list.append(char)
            else:
                a = 0
        else:
            if char.isdigit():
                if char == '0':
                    pass
                else:
                    my_list.append(char)
    i = ''.join(my_list)
    i = int(i)
    print(i)


if __name__ == '__main__':
    unchecked = input()
    is_integer(unchecked)
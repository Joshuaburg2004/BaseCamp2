def tc():
    i = input()
    my_list = []
    t = ""
    for a in i:
        if a.isdigit():
            my_list.append(a)
    if my_list[0] == my_list[1] == my_list[2]:
        t = "equilateral"
    elif my_list[0] == my_list[1] != my_list[2] or my_list[0] != my_list[1] == my_list[2] or my_list[0] == my_list[2] != my_list[1]:
        t = "isosceles"
    else:
        t = "scalene"
    return t


if __name__ == "__main__":
    q = tc()
    print(q)
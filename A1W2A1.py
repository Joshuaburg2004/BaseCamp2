def sd(a):
    a = a.split('-')
    if len(a) < 3 or len(a) > 3:
        if '/' in a[0] or '/' in a[1] or '_' in a[0] or '_' in a[1]:
            print("Input format ERROR. Correct Format: YYYY-MM-DD")
    if len(a[0]) < 4:
        print("Input format ERROR. Correct Format: YYYY-MM-DD")
    if a[0].isdigit() is False or a[1].isdigit() is False or a[2].isdigit() is False:
        print("ERROR: Please write an actual date. I.E: 2013-12-15.")
    if int(a[1]) > 12 or int(a[1]) < 1:
        print("ERROR: Month is the wrong size.")
    successor = suc(a)
    return successor


def suc(a):
    even = [4, 6, 9, 11]
    odd = [1, 3, 5, 7, 8, 10, 12]
    feb = [2]
    y = int(a[0])
    m = int(a[1])
    d = int(a[2])
    if m in even:
        if d > 30:
            print("ERROR: Day value to big.")
        else:
            if d == 30:
                d = 1
                m += 1
            else:
                d += 1
    elif m in odd:
        if d > 31:
            print("ERROR: Day value to big.")
        else:
            if d == 31:
                d = 1
                if m == 12:
                    m = 1
                    y += 1
                else:
                    m += 1
            else:
                d += 1
    elif m in feb:
        if d > 28:
            print("ERROR: Day value to big.")
        else:
            if d == 28:
                d = 1
                m += 1
            else:
                d += 1
    day = str(d)
    month = str(m)
    year = str(y)
    date = str(year.zfill(4)) + '-' + str(month.zfill(2)) + '-' + str(day.zfill(2))
    return date


if __name__ == '__main__':
    a = input()
    r = sd(a)
    print(f"Next date: {r}")
def check_triangle(a, b, c):
    l = [a, b, c]
    l.sort()
    s1 = l[0]
    s2 = l[1]
    s3 = l[2]
    if s3 >= s2 + s1:
        print('impossible')
    else:
        print('possible')


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    check_triangle(a, b, c)
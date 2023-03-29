def mult_table():
    header = '   1  2  3  4  5  6  7  8  9 10'
    my = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(header)
    for i in my:
        print(str(i), end=' ')
        for j in range(1, 10):
            print(str(j * i), end=' ')
        print(str(10 * i), end='\n')


if __name__ == '__main__':
    mult_table()
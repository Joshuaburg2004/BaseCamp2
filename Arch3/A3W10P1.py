import sys


def head(ine):
    a_list = []
    try:
        with open(ine, 'r') as f:
            data = f.readlines()
            for i in data:
                a_list.append(i)
        return a_list
    except FileNotFoundError:
        return False


def main():
    a_list = []
    try:
        ine = sys.argv[1]
        file = head(ine)
    except IndexError:
        print('File not found')
        return
    if file is False:
        print('ERROR')
        return
    for i in file:
        if len(a_list) <= 10:
            a_list.append(i)
    print(*a_list, sep='')


if __name__ == '__main__':
    main()
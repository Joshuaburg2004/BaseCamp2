def sorter(ine):
    my_list = []
    try:
        with open(ine, 'r') as f:
            for line in f:
                line = line.split(' ')
                for word in line:
                    word = word.strip()
                    my_list.sort(key=len)
                    if len(my_list) == 0:
                        my_list.append(word)
                    if len(my_list[0]) < len(word):
                        my_list.append(word)
            return my_list
    except FileNotFoundError:
        return False


def main():
    f = input('Give me a file: ')
    result = sorter(f)
    if result is not False:
        print(result)


if __name__ == '__main__':
    main()
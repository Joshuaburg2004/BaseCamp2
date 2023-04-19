def sorter(ine):
    my_list = []
    try:
        with open(ine, 'r') as f:
            longest = 0
            for line in f:
                line = line.split(' ')
                for word in line:
                    word = word.strip()
                    my_list.sort(key=len)
                    if longest < len(word):
                        my_list = []
                        my_list.append(word)
                        longest = len(word)
                    if longest == len(word):
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

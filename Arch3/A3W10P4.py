def occurences(ine):
    my_dict = {}
    try:
        with open(ine, 'r') as f:
            for line in f:
                line = line.split(' ')
                for word in line:
                    word = word.strip()
                    punc = '''!;:'",.?'''
                    res = ""
                    for char in word:
                        if char not in punc:
                            res += char
                    res = res.lower()
                    if res in my_dict.keys():
                        num = my_dict[res]
                        num += 1
                        my_dict[res] = num
                    else:
                        my_dict[res] = 1
        sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
        most = []
        least = []
        most_num = 0
        least_num = 1000
        for key, value in sorted_dict.items():
            if value == most_num:
                most.append(key)
            if value > most_num:
                most = []
                most.append(key)
                most_num = value
            if value == least_num:
                least.append(key)
            if value < least_num:
                least = []
                least.append(key)
                least_num = value
        print(most_num, least_num)
        return (most, least)
    except FileNotFoundError:
        return False, False


def main():
    ine = input('Give me a file: ')
    most, least = occurences(ine)
    if most is not False and least is not False:
        print(most)
        print(least)
    else:
        print('Error')


if __name__ == '__main__':
    main()
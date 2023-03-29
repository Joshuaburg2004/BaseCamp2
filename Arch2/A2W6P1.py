def unique_chars_dict(i):
    n = 0
    word_dict = {}
    for char in i:
        if char not in word_dict.values():
            n += 1
            word_dict[n] = char
        else:
            pass
    l = len(word_dict)
    print(l)
    return


def unique_chars_set(i):
    word_set = set({})
    for char in i:
        if char not in word_set:
            word_set.add(char)
        else:
            pass
    print(len(word_set))
    return


if __name__ == '__main__':
    putin = input('Give me a word: ')
    unique_chars_dict(putin)
    unique_chars_set(putin)
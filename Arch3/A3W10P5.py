def scrub(ine):
    res = ''
    try:
        with open(ine, 'r') as f:
            for line in f:
                if line[0] != '#':
                    res += line
            return res
    except FileNotFoundError:
        return False


def write_file(ine, content):
    with open(ine, 'w') as f:
        f.write(content)
        f.close()


def main():
    ine = input('File to read: ')
    ine2 = input('File to save: ')
    content = scrub(ine)
    if content is False:
        print('Error')
    else:
        write_file(ine2, content)


if __name__ == '__main__':
    main()
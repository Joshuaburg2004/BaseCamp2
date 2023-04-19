def scrub(ine):
    res = []
    try:
        with open(ine, 'r') as f:
            prevline = ''
            num = 1
            for line in f:
                aline = line.strip().split()
                if len(aline) > 1:
                    if aline[0] == 'def':
                        if prevline != '':
                            if prevline[0] != '#':
                                aline[1] = aline[1].strip(':')
                                res.append(f'File: {ine} contains a function [{aline[1]}] on line [{num}]\
 a without preceding comment.')
                        else:
                            aline[1] = aline[1].strip(':')
                            res.append(f'File: {ine} contains a function [{aline[1]}] on line [{num}]\
 a without preceding comment.')
                prevline = line
                num += 1
            return res
    except FileNotFoundError:
        return False


def main():
    ine = input('File to read: ').split(', ')
    for i in ine:
        content = scrub(i)
        if content is False:
            print('Error')
        for res in content:
            print(res)


if __name__ == '__main__':
    main()
    for i in ine:
        content = scrub(i)
        if content is False:
            print('Error')
        for res in content:
            print(res)


if __name__ == '__main__':
    main()

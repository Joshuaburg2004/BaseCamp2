mcd = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-',
    '?': '..--..', ' ': '    '}
mcdr = {v: k for k, v in mcd.items()}
my_l = ['.', '-', ' ']


def message_to_morse(msg):
    msg = msg.upper()
    morse = []
    for a in msg:
        if a not in mcd.keys():
            print(f"Can't convert char [{a}]")
        else:
            morse.append(mcd[a])
    return ' '.join(morse)


def morse_to_message(morse):
    msg = []
    msg_list = []
    if '    ' in morse:
        morse = morse.split('    ')
        for a in morse:
            a = a.split(' ')
            for m in a:
                b = check_if_morse(m)
                if b:
                    msg.append(mcdr[m])
                else:
                    return
            msg = ''.join(msg)
            msg_list.append(msg)
            msg = []
    else:
        morse = morse.split(' ')
        for a in morse:
            b = check_if_morse(a)
            if b:
                msg.append(mcdr[a])
            else:
                return
        msg = '' .join(msg)
        msg_list.append(msg)
    return ' '.join(msg_list)


def check_if_morse(a):
    for l in a:
        if l in my_l:
            continue
        else:
            print(f"Can't convert char [{l}]")
            return False
    return True


def translate_text(msg):
    msg = msg.upper()
    if all(char in my_l for char in msg):
        a = morse_to_message(msg)
    else:
        a = message_to_morse(msg)
    print(a)


def main():
    msg = input('Give me a message: ')
    translate_text(msg)


if __name__ == '__main__':
    main()
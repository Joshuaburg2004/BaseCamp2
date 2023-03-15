num_set = set('1234567890')
letter_set = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
char_set = {'*', '@', '!', '?'}


def num(pass_):
    pass_ = set(pass_)
    if len(pass_.intersection(num_set)) >= 1:
        return True
    else:
        return False


def letter(pass_):
    pass_ = set(pass_)
    if len(pass_.intersection(letter_set)) >= 1:
        return True
    else:
        return False


def char(pass_):
    pass_ = set(pass_)
    if len(pass_.intersection(char_set)) >= 1:
        return True
    else:
        return False


def check(pass_):
    pass_ = set(pass_)
    pass_.difference_update(num_set, letter_set, char_set)
    if len(pass_) >= 1:
        return False
    else:
        return True


def main():
    password = input('Give a password to check: ')
    num_check = num(password)
    letter_check = letter(password)
    char_check = char(password)
    check_ = check(password)
    if (num_check and letter_check and char_check and check_) is False:
        return False
    return True


if __name__ == "__main__":
    a = main()
    if a is True:
        print('This password is valid!')
    if a is False:
        print('This password is invalid!')

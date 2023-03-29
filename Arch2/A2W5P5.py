import random


def generate_random_password():
    pass_ = []
    length = random.randint(7, 10)
    for i in range(0, length):
        char = chr(random.randint(33, 126))
        pass_.append(char)
    pass_ = ''.join(pass_)
    return pass_


if __name__ == '__main__':
    a = generate_random_password()
    print(a)
dict_key_value = {}
encoded_values = []
decoded_values = []


def encode_string(data: str, key: str = None) -> str:
    if dict_key_value == {}:
        set_dict_key(key)
    output = ''.join(map(lambda char: dict_key_value.get(char, char), data))
    return output


def decode_string(data: str, key: str = None) -> str:
    if dict_key_value == {}:
        set_dict_key(key)
    dict_value_key = {v: k for k, v in dict_key_value.items()}
    output = ''.join(map(lambda char: dict_value_key.get(char, char), data))
    return output


def encode_list(data: list, key: str = None) -> list:
    output_list = []
    for item in data:
        output = encode_string(item, key)
        output_list.append(output)
    return output_list


def decode_list(data: list, key: str = None) -> list:
    output_list = []
    for item in data:
        output = decode_string(item, key)
        output_list.append(output)
    return output_list


def validate_values(encoded: str, decoded: str, key: str = None) -> bool:
    e = decode_string(encoded, key)
    if e == decoded:
        return True
    return False


def set_hashmap(key: str) -> None:
    if len(key) % 2 != 0:
        print("Invalid hashvalue input")
        print(key)
        return False
    else:
        return list(key)


def set_dict_key(key: str) -> None:
    if len(key) % 2 != 0:
        print("Invalid hashvalue input")
        print(key)
        return False
    else:
        key = list(key)
        dict_key_value.update(zip(key[::2], key[1::2]))


def main():
    key1 = input('Key: ')
    if key1 != '':
        key = key1
    else:
        key = 'a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$'
    move = ''
    check = set_hashmap(key)
    if check is False:
        move = 'Q'
    while move != 'Q':
        move = input('''[E] Encode value to hashed value
[D] Decode hashed value to normal value
[P] Print all encoded/decoded values
[V] Validate 2 values against eachother
[Q] Quit program\n''').upper()
        if move == 'E':
            i = input('Value to encode: ').split(', ')
            for item in encode_list(i, key):
                encoded_values.append(item)
        if move == 'D':
            i = input('Value to decode: ').split(', ')
            for item in decode_list(i, key):
                decoded_values.append(item)
        if move == 'P':
            for value in encoded_values:
                print(value)
            for value in decoded_values:
                print(value)
        if move == 'V':
            encode = input('Encoded value: ')
            decode = input('Decoded value: ')
            print(validate_values(encode, decode, key))
        if move == 'Q':
            break


if __name__ == "__main__":
    main()

dict_key_value = {}
dict_value_key = {}
encoded_values = []
decoded_values = []


# create a function that given the input string converts it to the encoded equivalent based on the provided or already set key/hashmap
# make sure to only convert values that are in the key, if the value is not present, use its own value
def encode_string(data: str, key: str = 'a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$') -> str:
    output = []
    dict_key_value = dict(zip(key[::2], key[1::2]))
    output = ''.join(map(lambda char: dict_key_value.get(char, char), data))
    return output


# create a function that given the input string converts it to the decoded equivalent based on the provided or already set key/hashmap
# make sure to only decode values that are in the key, if the value is not present, use its own value
def decode_string(data: str, key: str = 'a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$') -> str:
    dict_key_value = dict(zip(key[::2], key[1::2]))
    dict_value_key = {v: k for k, v in dict_key_value.items()}
    output = ''.join(map(lambda char: dict_value_key.get(char, char), data))
    return output

# create a function that given a list of inputs converts the complete list to the encoded equivalent based on the key/hashmap
# you can use the already created encode function when looping through the list
# tip! make use of the map function within python with a lambda to call the internal function with all elements
# as a return value, you should return a list with Tuples containing the decoded value as first value and the encode value as second value
def encode_list(data: list, key: str = 'a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$') -> list:
    output_list = []
    for item in data:
        output = encode_string(item, key)
        output_list.append(output)
    return output_list

# create a function that given a list of inputs converts the complete list to the encoded equivalent based on the key/hashmap
# you can use the already created decode function when looping through the list
# tip! make use of the map function within python with a lambda to call the internal function with all elements
# as a return value, you should return a list with Tuples containing the decoded value as first value and the encode value as second value
def decode_list(data: list, key: str = 'a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$') -> list:
    output_list = []
    for item in data:
        output = decode_string(item, key)
        output_list.append(output)
    return output_list


# create a function that given a encoded value, decoded value and a key (optional) checks if the values are correct
# the return value should be a boolean value (True if values match, False if they don't match)
def validate_values(encoded: str, decoded: str, key: str = None) -> bool:
    e = decode_string(encoded, key)
    if e == decoded:
        return True
    return False


# give the option to input a hashvalue to be used/converted to a key
# each oneven character is the Key of the Dict, each even character is the coresponding Value
# you should validate if the given input is an even input, otherwise show the error: Invalid hashvalue input
# example: a@b.c>d#eA will become: {'a': '@', 'b': '.', 'c': '>', 'd', '#', 'e': 'A'}
def set_hashmap(key: str) -> None:
    if len(key)%2 != 0:
        print("Invalid hashvalue input")
        print(key)
        return False
    else:
        return list(key)


# build menu structure as following
# the input can be case-insensitive (so E and e are valid inputs)
# [E] Encode value to hashed value
# [D] Decode hashed value to normal value
# [P] Print all encoded/decoded values
# [V] Validate 2 values against eachother
# [Q] Quit program
def main():
    key1 = input('Key: ')
    if key1 != '':
        key = key1
    else:
        key = 'a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$'
    key = set_hashmap(key)
    move = ''
    if key == False:
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


# Create a unittest for both the encode and decode function (see test_namehasher.py file for boilerplate)
if __name__ == "__main__":
    main()
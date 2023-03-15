def chess(chess_position):
    odd = ['A', 'C', 'E', 'G']
    even = ['B', 'D', 'F', 'H']
    letter = chess_position[0]
    number = int(chess_position[1])
    if letter in odd:
        if number % 2 == 0:
            print("White")
        else:
            print("Black")
    elif letter in even:
        if number % 2 == 0:
            print("Black")
        else:
            print("White")


if __name__ == "__main__":
    chess_position = input('Enter a chess position: ').upper()
    chess(chess_position)
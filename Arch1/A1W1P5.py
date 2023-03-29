if __name__ == "__main__":
    num = input("Please give me a number: ")
    if len(num) < 4 or len(num) > 4:
        print("This number is not the right length!")
    else:
        if num.isdigit():
            sum1 = 0
            my_list = []
            for i in num:
                i = int(i)
                sum1 += i
                my_list.append(i)
        else:
            print("ERROR: Your input has to be a number")
        a, b, c, d = my_list
        print(f"The sum of this number is {a}+{b}+{c}+{d}={sum1}")
def palindromecheck(p):
    p = p.strip('.,/?;:')
    p = p.lower()
    for i in range(0, int(len(p)/2)):
        if p[i] != p[len(p) - i - 1]:
            print(f"'{p}' is not a palindrome!")        
        else:
            continue
    print(f"'{p}' is a palindrome!")


if __name__ == '__main__':
    p = input()
    palindromecheck(p)
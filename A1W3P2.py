def palindromecheck(p):
    c = p.replace(' ', '')
    if c != c[::-1]:
        print(f"'{p}' is not a palindrome.")
    else:
        print(f"'{p}' is a palindrome.")


if __name__ == "__main__":
    p = input()
    palindromecheck(p)
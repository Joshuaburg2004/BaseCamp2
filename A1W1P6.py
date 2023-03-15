''' Input example:
Days: 1
Output example:
Hours: 24, Minutes: 1440, Seconds: 86400'''
def check(d):
    try:
        d = int(d)
    except ValueError:
        print("ERROR: Please input a (whole) number")
    return d


if __name__ == "__main__":
    d = input("Days: ")
    d = check(d)
    h = str(24 * d)
    m = str(60 * 24 * d)
    s = str(60 * 60 * 24 * d)
    print(f"Hours: {h}, Minutes: {m}, Seconds: {s}")
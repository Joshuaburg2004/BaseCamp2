def year_to_month(y):
    m = 12 * y
    m = str(m)
    return m


def year_to_day(y):
    d = 365 * y
    d = str(d)
    return d


if __name__ == "__main__":
    years = input("Years: ")
    if years.isdigit():
        years = int(years)
        months = year_to_month(years)
        days = year_to_day(years)
        print("Months:", months + ", Days:", days)
    else:
        print("ERROR: Please input a number")
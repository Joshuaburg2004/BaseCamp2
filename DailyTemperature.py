import os
import sys


date_dict = {1: 'January',
             2: 'February',
             3: 'March',
             4: 'April',
             5: 'May',
             6: 'June',
             7: 'July',
             8: 'August',
             9: 'September',
             10: 'October',
             11: 'November',
             12: 'December'}


def highest(year_dict):
    higher = 0
    temp_dict = average_temp_per_year(year_dict)
    for year in temp_dict:
        if year[1] > higher:
            higher = year[1]
            hottest_year = year[0]
    return hottest_year


def lowest(year_dict):
    lower = 10000000000000000000000000000
    temp_dict = average_temp_per_year(year_dict)
    for year in temp_dict:
        if year[1] < lower:
            lower = year[1]
            coldest_year = year[0]
    return coldest_year


def highest_month(year_dict):
    year = int(input('Give the year you wish to check: '))
    year_dict01 = year_dict[year]
    temp_list = []
    result = []
    higher = 0
    for month in year_dict01:
        appended = year_dict01[month]
        temp_list.append(appended)
    for temps in temp_list:
        a = round(sum(temps) / len(temps), 4)
        if a > higher:
            result = temp_list.index(temps) + 1
            higher = a
    return date_dict[result]


def lowest_month(year_dict):
    year = int(input('Give the year you wish to check: '))
    year_dict01 = year_dict[year]
    temp_list = []
    result = []
    lower = 10000000
    for month in year_dict01:
        appended = year_dict01[month]
        temp_list.append(appended)
    for temps in temp_list:
        a = round(sum(temps) / len(temps), 4)
        if a < lower:
            result = temp_list.index(temps) + 1
            lower = a
    return date_dict[result]


def average_temp_per_year(year_dict):
    temp_dict = []
    for i in year_dict:
        month_dict = year_dict[i]
        total = 0
        total_length = 0
        for month in month_dict:
            month_list = month_dict[month]
            summed = sum(month_list)
            total += summed
            total_length += len(month_list)
        temped = round((total / total_length), 4)
        temp = (i, temped)
        temp_dict.append(temp)
    return temp_dict


def average_temp_per_month(months):
    list_ = []
    for month in months.keys():
        month_list = months[month]
        summed = sum(month_list)
        avg = summed / len(month_list)
        avg_dict = (month, round(avg, 4))
        list_.append(avg_dict)
    return list_


def fahrenheit_to_celsius(F):
    C = (F - 32) * (5 / 9)
    return round(C, 4)


def data_cleaner(data):
    year_dict = {}
    month_dict = {}
    month = 0
    for list_ in data:
        if month != int(list_[0]):
            month_dict = {}
        try:
            lists = month_dict[int(list_[0])]
        except KeyError:
            lists = []
        try:
            month_dict = year_dict[int(list_[2])]
        except KeyError:
            month_dict = {}
        lists.append(float(list_[3]))
        month_dict[int(list_[0])] = lists
        year_dict[int(list_[2])] = month_dict
        month = int(list_[0])
    return year_dict


def load_txt_file(file_name):
    file_content = []
    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as file_obj:
        for line in file_obj.readlines():
            file_content.append(line.split())
    return file_content


def main():
    a = load_txt_file('NLAMSTDM.txt')
    year_dict = data_cleaner(a)
    i = int(input('''[1] Print the average temperature per year (fahrenheit)
[2] Print the average temperature per year (celsius)
[3] Print the warmest and coldest year as tuple based on average temperature
[4] Print the warmest month of a year based on the input of the user
[5] Print the coldest month of a year based on the input of the user
[6] Prints a list of tuples\n'''))
    if i == 1:
        temp_dict = average_temp_per_year(year_dict)
    if i == 2:
        temp = average_temp_per_year(year_dict)
        temp_dict = []
        for j in temp:
            year = j[0]
            temped = j[1]
            temped = fahrenheit_to_celsius(temped)
            j = (year, temped)
            temp_dict.append(j)
    if i == 3:
        higher = highest(year_dict)
        lower = lowest(year_dict)
        temp_dict = (higher, lower)
    if i == 4:
        temp_dict = highest_month(year_dict)
    if i == 5:
        temp_dict = lowest_month(year_dict)
    if i == 6:
        years = []
        for year in year_dict.keys():
            months = year_dict[year]
            avg_dict = average_temp_per_month(months)
            num_dict = {}
            for j in avg_dict:
                num = j[1]
                num = fahrenheit_to_celsius(num)
                num_dict[j[0]] = num
            years.append((year, num_dict))
        temp_dict = years
    print(temp_dict)


if __name__ == '__main__':
    main()
import os
import sys
import csv


def amount(file_cont, i):
    list_ = [y for y in file_cont if y[1] == i]
    return len(list_)


def get_headers(file_cont):
    headers = file_cont[0]
    return headers


def search_by_type(file_cont, show_type):
    list_ = list(filter(lambda x: (x[1] == show_type), file_cont))
    return list_


def search_by_director(file_cont, director):
    list_ = list(filter(lambda x: (x[3] == director), file_cont))
    return list_


def get_directors(file_cont):
    list_ = []
    for i in file_cont:
        if i[3] != '':
            list_.append(i[3])
    return list_


def director1(file_cont):
    dict_ = {}
    list_ = []
    for cinema in file_cont:
        if cinema[3] in dict_.keys():
            if cinema[1] != dict_[cinema[3]]:
                if cinema[3] != '':
                    if cinema[3] not in list_:
                        list_.append(cinema[3])
        else:
            dict_[cinema[3]] = cinema[1]
    return sorted(list_)


def director2(file_cont):
    dict_ = {}
    for cinema in file_cont:
        if cinema[3] != '':
            if cinema[3] in dict_.keys():
                if 'TV' in cinema[1]:
                    tv_num = dict_[cinema[3]][1] + 1
                    movie_num = dict_[cinema[3]][0]
                    dict_[cinema[3]] = (movie_num, tv_num)
                if 'Movie' in cinema[1]:
                    movie_num = dict_[cinema[3]][0] + 1
                    tv_num = dict_[cinema[3]][1]
                    dict_[cinema[3]] = (movie_num, tv_num)
            else:
                if 'TV' in cinema[1]:
                    dict_[cinema[3]] = (0, 1)
                if 'Movie' in cinema[1]:
                    dict_[cinema[3]] = (1, 0)
    res = dict_to_tuple(dict_)
    return res


def dict_to_tuple(dict_):
    list_ = []
    for person, nums in dict_.items():
        tuple_ = (person, nums[0], nums[1])
        list_.append(tuple_)
    return sorted(list_)


def load_csv_file(file_name):
    file_content = []
    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as csv_file:
        file_content = list(csv.reader(csv_file, delimiter=","))
    return file_content


def main():
    file_cont = load_csv_file('netflix_titles.csv')
    move = input('''[1] Print the amount of TV shows
[2] Print the amount of movies
[3] Print the full name of directors who direct both TV shows and movies
[4] Print the name of each director in alphabetical order with the number of shows and movies\n''')
    if move == '1':
        res = amount(file_cont, 'TV Show')
        print(res)
    if move == '2':
        res = amount(file_cont, 'Movie')
        print(res)
    if move == '3':
        res = director1(file_cont)
        print(res)
    if move == '4':
        res = director2(file_cont)
        print(res)


if __name__ == '__main__':
    main()

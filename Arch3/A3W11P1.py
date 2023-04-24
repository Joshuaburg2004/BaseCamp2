import os
import sys
import json


movie_list = []


def movie_information():
    result_list1 = []
    result_list2 = []
    result_list3 = []
    result_list4 = []
    for movie in movie_list:
        if movie['year'] == 2004:
            result_list1.append(movie)
        if 'Science Fiction' in movie['genres']:
            result_list2.append(movie)
        if 'Keanu Reeves' in movie['cast']:
            result_list3.append(movie)
        if 'Sylvester Stallone' in movie['cast'] and 1995 <= movie['year'] <= 2005:
            result_list4.append(movie)
    print(len(result_list1))
    print(len(result_list2))
    print(result_list3)
    print(result_list4)


def modifications():
    for movie in movie_list:
        if movie['title'] == 'Gladiator' and movie['year'] == 2000:
            movie['year'] = 2001
        if movie['year'] == 1900:
            movie['year'] = 1899
        if 'Natalie Portman' in movie['cast']:
            temp = movie['cast']
            temp.remove('Natalie Portman')
            temp.append('Nat Portman')
            movie['cast'] = temp
        if 'Kevin Spacey' in movie['cast']:
            temp = movie['cast']
            temp.remove('Kevin Spacey')
            movie['cast'] = temp


def search(title):
    for movie in movie_list:
        if movie['title'].lower() == title.lower():
            return movie


def search_mod(title):
    for movie in movie_list:
        if movie['title'].lower() == title.lower():
            movie['title'] = input('Give me a new title: ')
            movie['year'] = int(input('Give me a new release year: '))
            print(movie)


def read_from_json(filename):
    # read file
    with open(os.path.join(sys.path[0], filename), encoding='UTF-8') as outfile:
        data = json.load(outfile)
        # iterate over each line in data and call the add function
        for contact in data:
            movie_list.append(contact)


def write_to_json(filename):
    json_object = json.dumps(movie_list, indent=4)
    with open(os.path.join(sys.path[0], filename), "w", encoding='UTF-8') as outfile:
        outfile.write(json_object)


def main():
    read_from_json('movies.json')
    mover = ''
    while mover != 'q':
        mover = input('''[I] Movie information overview
[M] Make modification based on assignment
[S] Search a movie title
[C] Change title and/or release year by search on title
[Q] Quit program\n''').lower()
        if mover == 'i':
            movie_information()
        if mover == 'm':
            modifications()
            write_to_json('movies.json')
        if mover == 's':
            title = input('Give me a title: ')
            print(search(title))
        if mover == 'c':
            title = input('Give me a title: ')
            search_mod(title)
            write_to_json('movies.json')


if __name__ == "__main__":
    main()
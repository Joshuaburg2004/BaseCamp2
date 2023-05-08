import os
import sys
import csv


banned_video_games_list = []
header = []


def information():
    israel_count = 0
    country_dict = {}
    assassin_list = []
    assassin_int = 0
    german_list = []
    rdr_list = []
    for game in banned_video_games_list:
        _, title, series, country, details, _, status, _, _, _, _, _, _, _ = game
        if country == 'Israel':
            israel_count += 1
        if country in country_dict:
            country_dict[country] += 1
        if country not in country_dict:
            country_dict[country] = 0
        if series == "Assassin's Creed" and status == 'Active':
            if title not in assassin_list:
                assassin_int += 1
                assassin_list.append(title)
        if country == 'Germany':
            german_list.append((title, details))
        if title == 'Red Dead Redemption':
            rdr_list.append((country, details))
    print(israel_count)
    sorted_country_dict = dict(sorted(country_dict.items(), key=lambda item: item[1], reverse=True))
    print(list(sorted_country_dict.keys())[0])
    print(assassin_int)
    print(german_list)
    print(rdr_list)


def modifications():
    for game in banned_video_games_list:
        _, title, _, country, _, _, status, _, _, _, _, _, genre, _ = game
        if country == 'Germany':
            banned_video_games_list.remove(game)
        if title == 'Silent Hill VI':
            title = 'Silent Hill Remastered'
            removed = banned_video_games_list.index(game)
            game[1] = title
            banned_video_games_list.insert(removed, game)
        if title == 'Bully' and country == 'Brazil':
            if status == 'Ban Lifted':
                continue
            status = 'Ban Lifted'
            removed = banned_video_games_list.index(game)
            game[6] = status
            banned_video_games_list.insert(removed, game)
        if title == 'Manhunt II':
            if country == 'Germany':
                continue
            if genre == 'Action':
                continue
            genre = 'Action'
            removed = banned_video_games_list.index(game)
            game[12] = genre
            banned_video_games_list.insert(removed, game)


def add_game():
    id = input('<id>')
    title = input('<name>')
    series = input('<series>')
    country = input('<country>')
    details = input('<details>')
    category = input('<category>')
    status = input('<status>')
    wikipedia = input('<wikipedia>')
    image = input('<image>')
    summary = input('<summary>')
    developer = input('<developer>')
    publisher = input('<publisher>')
    genre = input('<genre>')
    homepage = input('<homepage>')
    game = [id, title, series, country, details, category, status, wikipedia, image, summary, developer, publisher, genre, homepage]
    banned_video_games_list.append(game)


def overview():
    country_dict = {}
    for game in banned_video_games_list:
        _, title, _, country, _, _, _, _, _, _, _, _, _, _ = game
        if country in country_dict:
            country_dict[country][0] += 1
            country_dict[country][1].append(title)
        if country not in country_dict:
            country_dict[country] = [1, [title]]
    print_overview(country_dict)


def print_overview(dicter):
    for country, value in dicter.items():
        print(country, "-", value[0])
        print(*value[1], sep='\n')


def search():
    search_country = input('Country to search by: ')
    country_dict = {}
    for game in banned_video_games_list:
        _, title, _, country, details, _, _, _, _, _, _, _, _, _ = game
        if country == search_country:
            country_dict[title] = details
    print_search(country_dict)


def print_search(dicter):
    for key, value in dicter.items():
        print(f'{key} - {value}')


def read_csv(filename):
    with open(os.path.join(sys.path[0], filename), newline='', encoding='UTF-8') as csv_file:
        head = (next(csv_file).split(','))
        for i in head:
            header.append(i.strip())
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            banned_video_games_list.append(line)


def write_to_csv():
    with open('new.csv', 'w', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(banned_video_games_list)


def main(filename):
    read_csv(filename)
    mover = ''
    while mover != 'q':
        mover = input('''[I] Print request info from assignment
[M] Make modification based on assignment
[A] Add new game to list
[O] Overview of banned games per country
[S] Search the dataset by country
[Q] Quit program\n''').lower()
        if mover == 'i':
            information()
        if mover == 'm':
            modifications()
        if mover == 'a':
            add_game()
        if mover == 'o':
            overview()
        if mover == 's':
            search()
        write_to_csv()


if __name__ == "__main__":
    main("bannedvideogames.csv")
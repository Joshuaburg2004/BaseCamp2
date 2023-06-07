import os
import sys
import json
import math
import sqlite3
from datetime import datetime, timedelta


books = []


def borrow_book():
    con = sqlite3.connect(os.path.join(sys.path[0], 'bookstore.db'))
    cur = con.cursor()
    cur.execute('''SELECT * FROM books WHERE status IS "BORROWED"''')
    data = cur.fetchall()
    cur1 = con.cursor()
    inputter = input('Give me an isbn or an id: ')
    date = input('Give me the days you wish to borrow it: ')
    if len(inputter) == 13:
        i = 'isbn'
    else:
        i = 'id'
    cur1.execute(f'''SELECT * FROM books WHERE {i} IS ?''', (inputter,))
    data1 = cur1.fetchall()
    if len(data1) == 0:
        return 'Book not found'
    if data1[0] in data:
        _, _, _, _, _, _, _, return_date = data[0]
        return f'This book has been borrowed already. This book can be borrowed again at {return_date}'
    current = datetime.now()
    days = int(date)
    return_date = current + timedelta(days = days)
    return_date_str = return_date.strftime('%d-%m-%Y')
    con.execute(f'''UPDATE books SET (status, return_date) = ("BORROWED", ?) WHERE {i} = ?''', (return_date, inputter))
    con.commit()
    con.close()
    return return_date_str


def return_book():
    con = sqlite3.connect(os.path.join(sys.path[0], 'bookstore.db'))
    now = datetime.now()
    cur = con.cursor()
    book = input('Give me your id or isbn: ')
    if len(book) == 13:
        i = 'isbn'
    else:
        i = 'id'
    cur.execute(f'''SELECT status, return_date FROM BOOKS WHERE {i} = ?''', (book,))
    data = cur.fetchall()
    data = data[0]
    if len(data) == 0 or data[0] == "AVAILABLE":
        con.close()
        return 'Book not borrowed/found'
    else:
        timechange = now - datetime.strptime(data[1], '%Y-%m-%d %H:%M:%S.%f')
        if timechange > timedelta(days=0):
            number = timechange.days
            result = number * 0.5
            con.execute(f'''UPDATE books SET (status, return_date) = ("AVAILABLE", NULL) WHERE {i} = ?''', (book,))
            con.commit()
            con.close()
            return f'{result} EUR'
        else:
            con.execute(f'''UPDATE books SET (status, return_date) = ("AVAILABLE", NULL) WHERE {i} = ?''', (book,))
            con.commit()
            con.close()
            return 'returned'


def search_book():
    con = sqlite3.connect(os.path.join(sys.path[0], 'bookstore.db'))
    search_term = input('Search: ')
    alpha = False
    if search_term.isnumeric():
        if len(search_term) == 13:
            i = 'isbn'
        else:
            i = 'id'
    else:
        alpha = True
    cur = con.cursor()
    if alpha:
        cur1 = con.cursor()
        cur.execute('''SELECT * FROM books WHERE author = ?''', (search_term,))
        data = cur.fetchall()
        cur1.execute('''SELECT * FROM books WHERE title = ?''', (search_term,))
        data1 = cur1.fetchall()
        if len(data) == 0 and len(data1) != 0:
            con.close()
            return data1[0]
        else:
            con.close()
            return data[0]
    else:
        cur.execute(f'''SELECT * FROM books WHERE {i} = ?''', (search_term,))
        data = cur.fetchall()
        con.close()
        try:
            return data[0]
        except IndexError:
            return


def read_from_json(filename):
    # read file
    with open(os.path.join(sys.path[0], filename)) as outfile:
        data = json.load(outfile)
        for i in data:
            books.append(i)



def main():
    read_from_json('books.json')
    con = sqlite3.connect(os.path.join(sys.path[0], 'bookstore.db'))
    con.execute(
        '''CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn TEXT NOT NULL,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            pages INTEGER NOT NULL,
            year TEXT NOT NULL,
            status TEXT DEFAULT "AVAILABLE",
            return_date DATE DEFAULT NULL
        );'''
    )
    for i in books:
        isbn, title, author, pages, year = i.values()
        sql = "INSERT OR IGNORE INTO books (isbn, title, author, pages, year) VALUES (?, ?, ?, ?, ?)"
        val = (isbn, title, author, pages, year)
        con.execute(sql, val)
        con.commit()
    mover = ""
    while mover != 'q':
        mover = input('''[B] Borrow book
[R] Return book
[S] Search book
[Q] Quit program\n''').lower()
        if mover == 'b':
            print(borrow_book())
        if mover == 'r':
            print(return_book())
        if mover == 's':
            data = search_book()
            data_dict = {}
            if data is not None:
                data_dict['id'] = data[0]
                data_dict['isbn'] = data[1]
                data_dict['title'] = data[2]
                data_dict['author'] = data[3]
                data_dict['pages'] = data[4]
                data_dict['year'] = data[5]
                data_dict['status'] = data[6]
                data_dict['return_date'] = data[7]
                print(data_dict)
    con.close()


if __name__ == "__main__":
    main()
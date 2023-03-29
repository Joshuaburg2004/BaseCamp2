library = []


def add_title():
    book_title, book_author, publisher, publication_date = input('Book details: ').lower().split(',')
    book_list = {'title': book_title, 'author': book_author, 'publisher': publisher, 'pub_date': publication_date}
    inned = False
    for v in library:
        if book_title in v:
            return
    if inned is False:
        library.append(book_list)
        return book_list


def search_book(books, term):
    term = term.lower()
    found = False
    if books == "":
        books = library
    for item in books:
        if term in item.values():
            found = True
        else:
            continue
    return found


def main():
    a = ''
    result = []
    while a != 'e':
        a = input('[A] Add book\n[S] Search book\n[E] Exit (and print)\n').lower()
        if a == 'a':
            b = add_title()
            result.append(b)
        if a == 's':
            term = input('Search term: ')
            q = search_book(library, term)
            if q is True:
                print(f'Found book for{term}')
        if a == 'e':
            print('\n'.join(repr(e) for e in result))
            break


if __name__ == '__main__':
    main()
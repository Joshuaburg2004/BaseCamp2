import os
import sys
import sqlite3


def add_new_student():
    con = sqlite3.connect(os.path.join(sys.path[0], 'studentdatabase.db'))
    first_name = input("First name: ")
    last_name = input("Last name: ")
    city = input("City: ")
    date_of_birth = input("Date of birth: ")
    day, month, year = date_of_birth.split('-')
    if 31 < int(day) < 0 or 0 > int(month) > 12:
        print('Error, wrong date format')
    class_ = input("class: ")
    if class_ == '':
        sql = "INSERT INTO students (first_name, last_name, city, date_of_birth) VALUES (?, ?, ?, ?)"
        val = (first_name, last_name, city, date_of_birth)
        con.execute(sql, val)
    else:
        sql = "INSERT INTO students (first_name, last_name, city, date_of_birth, class) VALUES (?, ?, ?, ?, ?)"
        val = (first_name, last_name, city, date_of_birth, class_)
        con.execute(sql, val)
    data = con.cursor().execute('''SELECT studentnumber FROM students ORDER BY studentnumber DESC LIMIT 1''').fetchone()
    con.commit()
    con.close()
    return data

# first_name, last_name, city, date_of_birth (DD-MM-YYYY), class (optional)
def assign_to_class():
    student_number = input('Search number: ')
    con = sqlite3.connect(os.path.join(sys.path[0], 'studentdatabase.db'))
    cur = con.cursor()
    cur.execute("SELECT * FROM students WHERE studentnumber = ?", (student_number,))
    data = cur.fetchall()
    if len(data) == 0:
        return False, student_number
    student_number, first_name, last_name, city, date_of_birth, class_ = data[0]
    class_ = input('Assign a class: ')
    data = student_number, first_name, last_name, city, date_of_birth, class_
    con.execute("UPDATE students SET class = ? WHERE studentnumber = ?", (class_, student_number))
    con.commit()
    con.close()
    return class_


def list_all_stud():
    con = sqlite3.connect(os.path.join(sys.path[0], 'studentdatabase.db'))
    cur = con.execute('''SELECT * FROM students ORDER BY class DESC''')
    data = cur.fetchall()
    con.close()
    return data


def list_by_class(listed):
    con = sqlite3.connect(os.path.join(sys.path[0], 'studentdatabase.db'))
    cur = con.execute('''SELECT * FROM students WHERE class = ? ORDER BY studentnumber ASC''', (listed,))
    data = cur.fetchall()
    con.close()
    return data


def search(term):
    con = sqlite3.connect(os.path.join(sys.path[0], 'studentdatabase.db'))
    cur = con.execute('SELECT * FROM students WHERE first_name = ? LIMIT 1', (term,)).fetchall()
    cur1 = con.execute('SELECT * FROM students WHERE last_name = ? LIMIT 1', (term,)).fetchall()
    cur2 = con.execute('SELECT * FROM students WHERE class = ? LIMIT 1', (term,)).fetchall()
    if len(cur) > 0:
        con.close()
        return cur
    if len(cur1) > 0:
        con.close()
        return cur1
    if len(cur2) > 0:
        con.close()
        return cur2
    con.close()


def main():
    con = sqlite3.connect(os.path.join(sys.path[0], 'studentdatabase.db'))
    con.execute(
        '''CREATE TABLE IF NOT EXISTS students (
            studentnumber INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            city TEXT NOT NULL,
            date_of_birth DATE NOT NULL,
            class TEXT DEFAULT NULL 
        );'''
    )
    inputter = ''
    while inputter != 'Q':
        inputter = input('''[A] Add new student
[C] Assign student to class
[D] List all students
[L] List all students in class
[S] Search student
[Q] Quit program\n''').upper()
        if inputter == 'A':
            student_number = add_new_student()
            print(student_number)
        if inputter == 'C':
            class_, number = assign_to_class()
            if class_ is False:
                print(f"Could not find student with number: {number}")
        if inputter == 'D':
            students = list_all_stud()
            for student in students:
                print(student)
        if inputter == 'L':
            listed = input('Give me a class: ')
            result = list_by_class(listed)
            for i in result:
                print(i)
        if inputter == 'S':
            term = input('give me a name or a city: ')
            result = search(term)
            print(result)
        con.commit()
    con.close()


if __name__ == "__main__":
    main()

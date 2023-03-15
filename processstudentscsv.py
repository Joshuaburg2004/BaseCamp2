import os
import sys

valid_lines = []
corrupt_lines = []


def num_validate(student_number):
    num_inv = False
    if student_number[0:2] not in ['08', '09']:
        num_inv = True
    if student_number.isnumeric() is not True:
        num_inv = True
    return num_inv


def name_validate(name):
    inv = False
    if name.isalpha() is not True:
        inv = True
    return inv


def date_validate(date):
    date_inv = False
    try:
        year, month, day = date.split('-')
    except ValueError:
        date_inv = True
    if date_inv is not True:
        if len(year) != 4 or len(month) != 2 or len(day) != 2:
            date_inv = True
        if int(year) > 2004 or int(year) < 1960:
            date_inv = True
        if int(month) < 1 or int(month) > 12:
            date_inv = True
        if int(day) < 1 or int(day) > 31:
            date_inv = True
    return date_inv


def study_validate(study):
    inv = False
    if study not in ['INF', 'TINF', 'CMD', 'AI']:
        inv = True
    return inv


def validate_data(line):
    student_number, first_name, last_name, date_of_birth, study_program = line.split(',')
    invalid_data = []
    num_inv = num_validate(student_number)
    first_inv = name_validate(first_name)
    last_inv = name_validate(last_name)
    date_inv = date_validate(date_of_birth)
    study_inv = study_validate(study_program)
    inv = num_inv or first_inv or last_inv or date_inv or study_inv
    if inv is False:
        valid_lines.append(line)
        return
    if num_inv is True:
        invalid_data.append(student_number)
    if first_inv is True:
        invalid_data.append(first_name)
    if last_inv is True:
        invalid_data.append(last_name)
    if date_inv is True:
        invalid_data.append(date_of_birth)
    if study_inv is True:
        invalid_data.append(study_program)
    a = line + f' => INVALID DATA: {invalid_data}'
    corrupt_lines.append(a)


def main(csv_file):
    with open(os.path.join(sys.path[0], csv_file), newline='') as csv_file:
        next(csv_file)
        for line in csv_file:
            validate_data(line.strip())
    print('### VALID LINES ###')
    print("\n".join(valid_lines))
    print('### CORRUPT LINES ###')
    print("\n".join(corrupt_lines))


if __name__ == "__main__":
    main('students.csv')
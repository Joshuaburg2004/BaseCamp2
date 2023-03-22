import os
import sys
import json

addressbook = []


# print all contacts in the following format:
# ======================================
# Position: <position>
# First name: <firstname>
# Last name: <lastname>
# Emails: <email_1>, <email_2>
# Phone numbers: <number_1>, <number_2>
def display(list_=[]):
    for i in list_:
        print(f'Position: {i["id"]}')
        print(f'First name: {i["first_name"]}')
        print(f'Last name: {i["last_name"]}')
        print('Emails: ', end='')
        for item in i['emails']:
            if i['emails'].index(item) == len(i['emails']) - 1:
                print(item)
            else:
                print(item, end=', ')
        print('Phone numbers: ', end='')
        for item in i['phone_numbers']:
            if i['phone_numbers'].index(item) == len(i['phone_numbers']) - 1:
                print(item)
            else:
                print(item, end=', ')
        print('======================================')
    return


# return list of contacts sorted by first_name or last_name [if blank then unsorted], direction [ASC (default)/DESC])
def list_contacts():
    # todo: implement this function
    display(addressbook)
    return


# add new contact:
# - first_name
# - last_name
# - emails = {}
# - phone_numbers = {}
def add_contact(id_, first_name, last_name, emails, phone_numbers):
    # todo: implement this function
    contact = {}
    contact['id'] = id_
    contact['first_name'] = first_name
    contact['last_name'] = last_name
    contact['emails'] = emails
    contact['phone_numbers'] = phone_numbers
    addressbook.append(contact)
    return


# remove contact by ID (integer)
def remove_contact(id_):
    # todo: implement this function
    for contact in addressbook:
        if contact["id"] == id_:
            addressbook.remove(contact)
            return


# merge duplicates (automated > same fullname [firstname & lastname])
def merge_contacts():
    # todo: implement this function
    name_list = []
    for contact in addressbook:
        con_list = [contact['first_name'], contact['last_name']]
        if con_list not in name_list:
            name_list.append(con_list)
        else:
            emails = contact['emails']
            phone_numbers = contact['phone_numbers']
            id_ = name_list.index(con_list) + 1
            addressbook.remove(contact)
            for contact in addressbook:
                if contact['id'] == id_:
                    e = contact['emails']
                    p = contact['phone_numbers']
                    for item in emails:
                        if item not in e:
                            e.append(item)
                    for items in phone_numbers:
                        if items not in p:
                            p.append(items)
                    contact['emails'] = e
                    contact['phone_numbers'] = p
                    addressbook.remove(contact)
                    addressbook.insert(id_ - 1, contact)


# read_from_json
# Do NOT change this function
def read_from_json(filename):
    # read file
    with open(os.path.join(sys.path[0], filename)) as outfile:
        data = json.load(outfile)
        # iterate over each line in data and call the add function
        for contact in data:
            addressbook.append(contact)


# write_to_json
# Do NOT change this function
def write_to_json(filename):
    json_object = json.dumps(addressbook, indent=4)
    with open(os.path.join(sys.path[0], filename), "w") as outfile:
        outfile.write(json_object)


# main function:
# # build menu structure as following
# # the input can be case-insensitive (so E and e are valid inputs)
# # [L] List contacts
# # [A] Add contact
# # [R] Remove contact
# # [M] Merge contacts
# # [Q] Quit program
# Don't forget to put the contacts.json file in the same location as this file!
def main(json_file):
    read_from_json(json_file)
    move = ''
    while move != 'Q':
        move = input('''[L] List contacts
[A] Add contact
[R] Remove contact
[M] Merge contacts
[Q] Quit program\n''').upper()
        if move == 'L':
            list_contacts()
        if move == 'A':
            id_ = len(addressbook) + 1
            first = False
            last = False
            while first is False:
                first_name = input('First name: ')
                if all(x.isalpha() or x.isspace() for x in first_name):
                    first = True
            while last is False:
                last_name = input('Last name: ')
                if all(x.isalpha() or x.isspace() for x in last_name):
                    last = True
            e = input('Email: ').split(',')
            emails = []
            for email in e:
                if '@' in email and email != '':
                    emails.append(email)
                if email == '' and len(emails) > 0:
                    break
            p = input('Phone number: ').split(',')
            phone_numbers = []
            for phone_number in p:
                if phone_number.isdigit() and phone_number != '':
                    phone_numbers.append(phone_number)
                if phone_number == '' and len(phone_numbers) > 0:
                    break
            add_contact(id_, first_name, last_name, emails, phone_numbers)
        if move == 'R':
            id_ = int(input('Which contact do you want to remove? '))
            remove_contact(id_)
        if move == 'M':
            merge_contacts()
        if move == 'Q':
            sys.exit()
        write_to_json('contacts.json')


if __name__ == "__main__":
    main('contacts.json')

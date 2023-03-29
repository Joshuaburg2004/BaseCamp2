#Code for the offer letter
def offer():
    salary_confirm = False
    first_confirm = False
    last_confirm = False
    title_confirm = False
    start_confirm = False
    #Using while to reuse the input until it is correct
    while first_confirm is False:
        first = input()
        if first.isalpha() is False or first[0].isupper() is False or 2 > len(first) or len(first) > 10:
            first_confirm = False
            print('Input error')
        else:
            first_confirm = True
    while last_confirm is False:
        last = input()
        if last.isalpha() is False or last[0].isupper() is False or 2 > len(last) or len(last) > 10:
            last_confirm = False
            print('Input error')
        else:
            last_confirm = True
    while title_confirm is False:
        title = input()
        if all(x.isalpha() or x.isspace() for x in title) is False or len(title) < 10:
            title_confirm = False
            print('Input error')
        else:
            title_confirm = True
    while salary_confirm is False:
        salary = input()
        sf = salary.replace(',', '.')
        sf = sf.replace('.', '', 1)
        try:
            sf = float(sf)
            if 20000 > sf or 80000 < sf:
                salary_confirm = False
                print('Input error')
            else:
                salary_confirm = True
        except ValueError:
            salary_confirm = False
            print('Input error')
    while start_confirm is False:
        start = input()
        try:
            year, month, day = start.split('-')
            iyear = int(year)
            imonth = int(month)
            iday = int(day)
            if month == None or day == None or year == None or imonth <= 0 or imonth > 12 or iday <= 0 or iday > 31 or (iyear != 2021 and iyear != 2022):
                start_confirm = False
                print('Input error')
            else:
                start_confirm = True
        except ValueError:
            start_confirm = False
            print('Input error')
    #Double check to see if everything is correct.
    if salary_confirm is True and first_confirm is True and last_confirm is True and title_confirm is True and start_confirm is True:
        print('Here is the final letter to send:')
        print(f'Dear {first} {last},')
        print(f'After careful evaluation of your application for the position of {title},')
        print(f'we are glad to offer you the job. Your salary will be {salary} euro annually.')
        print(f'Your start date will be on {start}. Please do not hesitate to contact us with any questions.')
        print('Sincerely,')
        print('HR Department of XYZ')
    return


#Code for the rejection letter
def rejection():
    first_confirm = False
    last_confirm = False
    title_confirm = False
    char = ['+']
    #While is used to reuse the input of all parts, until it is correct.
    while first_confirm is False:
        first = input()
        if first.isalpha() is False or first[0].isupper() is False or 2 > len(first) or len(first) > 10:
            first_confirm = False
            print('Input error')
        else:
            first_confirm = True
    while last_confirm is False:
        last = input()
        if last.isalpha() is False or last[0].isupper() is False or 2 > len(last) or len(last) > 10:
            last_confirm = False
            print('Input error')
        else:
            last_confirm = True
    while title_confirm is False:
        title = input()
        if all(x.isalpha() or x.isspace() or x in char for x in title) is False or len(title) < 10:
            title_confirm = False
            print('Input error')
        else:
            title_confirm = True
    #Check if the user wants to give feedback
    feedback_bool = input().lower()
    if feedback_bool == "yes":
        feedback = input()
    #double check that nothing is wrong
    if first_confirm is True and last_confirm is True and title_confirm is True:
        print('Here is the final letter to send:')
        print(f'Dear {first} {last},')
        print(f'After careful evaluation of your application for the position of {title}, ')
        print('at this moment we have decided to proceed with another candidate. ')
        if feedback_bool == "yes":
            print('Here we would like to provide you our feedback about the interview.')
            print(feedback)
        print('We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions. ')
        print('Sincerely,')
        print('HR Department of XYZ')
    return


#Logic to give the user the options they need.
def total():
    more = ""
    while more.lower() != "no":
        more = input()
        if more != "no":
            try:
                type_ = input()
                if type_.lower() == "job offer":
                    offer()
                if type_.lower() == "rejection":
                    rejection()
            except EOFError:
                exit()


#Always run the logic whenever it starts
if __name__ == "__main__":
    total()
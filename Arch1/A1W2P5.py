#function define to run code.
def holiday_check(a):
    my_list = {"1-1": "Nieuwjaarsdag",
    "4-7": "Goede vrijdag",
    "4-9": "Eerste paasdag",
    "4-10": "Tweede paasdag",
    "4-27": "Koningsdag",
    "5-5": "Bevrijdingsdag",
    "5-18": "Hemelvaartsdag",
    "5-28": "Eerste pinksterdag",
    "5-29": "Tweede pinksterdag",
    "12-25": "Eerste kerstdag",
    "12-26": "Tweede kerstdag"}
    prev = ""
    l = []
    #variable to check if correct
    appended = False
    #loops through input and takes numbers out. Throws into a list. Uses list to make end date.
    for i in a:
        if i.isdigit():
            if prev.isdigit():
                s = str(prev) + str(i)
                l.append(s)
                prev = ""
                appended = True
            else:
                prev = i
                appended = False
        else:
            if prev.isdigit():
                if appended == True:
                    appended = False
                    prev = i
                else:
                    s = str(prev)
                    l.append(s)
                    prev = ""
                    appended = True
            else:
                prev = i
                appended = False
    if i.isdigit() and appended is False:
        l.append(i)
    date = l[0] + "-" + l[1]
    try:
        print(my_list[date])
    except KeyError:
        print("This is not a holiday.")

        
if __name__ == "__main__":
    a = input()
    holiday_check(a)
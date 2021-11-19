# Mehta Nimtrakul
# I pledge my honor that I have abided by the Stevens Honor System. 
# US35
# list recent births

from datetime import datetime


def RecentBirths(file):
    # Returns list of people who were born in the last 30 days
    f = open(file, "r")
    lst = []
    for line in f:
        lst.append(line.replace('\n', ''))
    recent = []
    date = datetime.now()
    for i in range(len(lst)):
        if "BIRT" in lst[i]:
            lst2 = lst[i+1].split(' ')
            birthdate = datetime.strptime(lst2[2]+lst2[3]+lst2[4] ,'%d%b%Y')
            if ((date - birthdate).days) <= 30:
                recent.append(lst[i-5].split(' ')[2]+lst[i-5].split(' ')[3].replace("/", " ").rstrip())
    if recent == []:
        print("No recent births")
    else:
        print(recent)

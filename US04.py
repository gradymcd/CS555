#US 04
from datetime import datetime

def RecentDeaths(file):
    # Returns list of people who died in the last 30 days
    f = open(file, "r")
    lst = []
    for line in f:
        lst.append(line.replace('\n', ''))
    deaths = []
    recent = []
    date = datetime.now()
    for i in range(len(lst)):
        if "DEAT" in lst[i]:
            lst2 = lst[i+1].split(' ')
            deathdate = datetime.strptime(lst2[2]+lst2[3]+lst2[4] ,'%d%b%Y')
            if ((date - deathdate).days) <= 30:
                recent.append(lst[i-7].split(' ')[2]+lst[i-7].split(' ')[3].replace("/", " ").rstrip())
    if recent == []:
        print("No recent deaths")
    else:
        print(recent)
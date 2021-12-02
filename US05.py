#US 05
from datetime import datetime

def MarriageDeath(file):
    # Returns false if there is a death before marriage
    f = open(file, "r")
    lst = []
    for line in f:
        lst.append(line.replace('\n', ''))
    date = datetime.now()
    for i in range(len(lst)):
        if "DEAT" in lst[i]:
            lst2 = lst[i+1].split(' ')
            deathdate = datetime.strptime(lst2[2]+lst2[3]+lst2[4] ,'%d%b%Y')
    for j in range(len(lst)):
        if "MARR" in lst[j]:
            lst2 = lst[j+1].split(' ')
            marrdate = datetime.strptime(lst2[2]+lst2[3]+lst2[4] ,'%d%b%Y')
    if deathdate > marrdate:
        return True
    return False  
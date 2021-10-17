# Mehta Nimtrakul
# I pledge my honor that I have abided by the Stevens Honor System. 
# US23

def UniqueNameBirthdate(file):
    f = open(file, "r")
    lst = []
    for line in f:
        lst.append(line.replace('\n', ''))
    indis = []
    my_set = set()
    
    for i in range(len(lst)):
        if "INDI" in lst[i]:
            indis.append(lst[i+1])
        if "BIRT" in lst[i]:
            indis.append(lst[i+1])
    for i in range(len(indis)):
        if "NAME" in indis[i]:
            my_set.add(indis[i]+indis[i+1])
    if(len(my_set)) < len(indis)/2:
        return False
    else:
        return True 

    



    
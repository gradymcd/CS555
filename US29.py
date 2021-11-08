# Mehta Nimtrakul
# I pledge my honor that I have abided by the Stevens Honor System. 
# US29
# list deceased



def ListDeceased(file):
    f = open(file, "r")
    lst = []
    for line in f:
        lst.append(line.replace('\n', ''))
    deceased = []
    for i in range(len(lst)):
        if "DEAT" in lst[i]:
            deceased.append(lst[i-7].split(' ')[2]+lst[i-7].split(' ')[3].replace("/", " ").rstrip())
    
    print("Deceased:", deceased)



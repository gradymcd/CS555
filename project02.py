TagLevels = {
    "INDI": 0,
    "NAME": 1,
    "SEX":  1,
    "BIRT": 1,
    "DEAT": 1,
    "FAMC": 1,
    "FAMS": 1,
    "FAM":  0,
    "MARR": 1,
    "HUSB": 1,
    "WIFE": 1,
    "CHIL": 1,
    "DIV":  1,
    "DATE": 2,
    "HEAD": 0,
    "TRLR": 0,
    "NOTE": 0
}

file = open(input('File: '), 'r')
lines = file.readlines()

for line in lines:
    line = line.replace('\n', ' ')
    print('--> ' + line)
    
    elems = line.split(' ')
    level = elems[0]
    if("INDI" in elems or "FAM" in elems):
        tag = elems[2]
        args = [elems[1]]
    else:
        tag = elems[1]
        args = elems[2:]  
    valid = 'N'
    if(tag in TagLevels.keys()):
                valid = 'Y'
    
    print('<-- ' + level + '|' + tag + '|' + valid + '|', end='')
    for arg in args:
            print(arg, end=' ')
    print()

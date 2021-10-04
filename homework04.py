from datetime import datetime


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

def checkGed(filePath, debug=False):
    line = ''
    lineI = 0
    level = ''
    tag = ''
    valid = ''
    args = []

    def printLine():
        print(level + '|' + tag + '|' + valid + '|', end='')
        for arg in args:
            print(arg, end=' ')
        print()
        
    file = open(filePath, 'r')
    res = ''
    lines = file.readlines()
    areErrors = False

    for line in lines:
        lineI += 1
        line = line.replace('\n', ' ')
        
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
        
        if(tag == 'DATE' and datetime.strptime(args[0] + args[1] + args[2], '%d%b%Y')>datetime.now()):
            res += 'ERROR US01 on line ' + str(lineI) + ': Dates (birth, marriage, divorce, death) should not be after the current date'
            if(debug):
                printLine()
            areErrors = True

    if(not areErrors):
        res += 'No errors'

    file.close()
    return res

if __name__ == '__main__':
    file = input('File: ')
    print(checkGed(file), True)

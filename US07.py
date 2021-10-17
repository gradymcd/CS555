# Mehta Nimtrakul
# I pledge my honor that I have abided by the Stevens Honor System. 
# US07 - Less than 150 years old

def LessThan150(file):
    f = open(file, "r")
    lst = []
    for line in f:
        lst.append(line.replace('\n', ''))
    
    for i in range(len(lst)):
        if "BIRT" in lst[i]:
            if (2021 - int(lst[i+1][-4:])) >= 150:
                if "DEAT" not in lst[i+2]:
                    print(f"Error US07: on line {i+2}, there should not be a person alive after 150 years")
                    return True 
        else:
            continue 
    return False 


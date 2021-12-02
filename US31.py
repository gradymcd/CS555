#List living single

def listLivingSingle(indis):
    lst = []
    for person in indis:
        if indis[person]['Alive'] and indis[person]['Spouse'] == 'NA':
            lst.append(indis[person]['Name'])

    return lst
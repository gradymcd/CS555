#US 21: Correct gender for role

def corrGen(indis, fams):
    for key, val in fams.items():
        # assume we have both husb and wife all the time
        husbId = val['Husband ID']
        wifeId = val['Wife ID']
        if indis[husbId]['Gender'] != 'M':
            print('Error: US21: Individual {} is not the correct gender M in family {}'.format(husbId, key))
        if indis[wifeId]['Gender'] != 'F':
            print('Error: US21: Individual {} is not the correct gender F in family {}'.format(wifeId, key))

    return
import unittest
#US 21: Correct gender for role

def corrGen(indis, fams):
    valid = True
    for key, val in fams.items():
        # assume we have both husb and wife all the time
        husbId = val['Husband ID']
        wifeId = val['Wife ID']
        if indis[husbId]['Gender'] != 'M':
            print('Error: US21: Individual {} is not the correct gender M in family {}'.format(husbId, key))
            valid = False
        if indis[wifeId]['Gender'] != 'F':
            print('Error: US21: Individual {} is not the correct gender F in family {}'.format(wifeId, key))
            valid = False

    return valid

class TestUS31(unittest.TestCase):
    def test1(self):
        indis = {
            'I1': {
                'Name': 'I1',
                'Gender': 'M'
            },
            'I2': {
                'Name': 'I2',
                'Gender': 'F'
            },
            'I3': {
                'Name': 'I2',
                'Gender': 'M'
            }
        }
        fams = {
            'F1': {
                'Husband ID': 'I2',
                'Wife ID': 'I3',
                'Children': ['I1']
            }}
        self.assertFalse(corrGen(indis, fams))

    def test2(self):
        indis = {
            'I1': {
                'Name': 'I1',
                'Gender': 'M'
            },
            'I2': {
                'Name': 'I2',
                'Gender': 'F'
            },
            'I3': {
                'Name': 'I2',
                'Gender': 'M'
            }
        }
        fams = {
            'F1': {
                'Husband ID': 'I1',
                'Wife ID': 'I2',
                'Children': []
            }}
        self.assertTrue(corrGen(indis, fams))

    def test3(self):
        indis = {
            'I1': {
                'Name': 'I1',
                'Gender': 'M'
            },
            'I2': {
                'Name': 'I2',
                'Gender': 'F'
            },
            'I3': {
                'Name': 'I2',
                'Gender': 'M'
            }
        }
        fams = {}
        self.assertTrue(corrGen(indis, fams))

if __name__ == '__main__':
    unittest.main()
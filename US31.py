import unittest
#List living single

def listLivingSingle(indis):
    lst = []
    for person in indis:
        if indis[person]['Alive'] and indis[person]['Spouse'] == 'NA':
            lst.append(indis[person]['Name'])

    return lst

class TestUS31(unittest.TestCase):
    def test1(self):
        indis = {
        'I1': {
            'Name': 'I1',
            'Alive': True,
            'Spouse': 'NA'
        },
        'I2': {
            'Name': 'I2',
            'Alive': True,
            'Spouse': 'NA'
        },
        'I3': {
            'Name': 'I3',
            'Alive': True,
            'Spouse': 'NA'
        }}
        self.assertEqual(listLivingSingle(indis), ['I1', 'I2', 'I3'])

    def test2(self):
        indis = {
        'I1': {
            'Name': 'I1',
            'Alive': True,
            'Spouse': 'NA'
        },
        'I2': {
            'Name': 'I2',
            'Alive': False,
            'Spouse': 'NA'
        },
        'I3': {
            'Name': 'I3',
            'Alive': False,
            'Spouse': 'NA'
        }}
        self.assertEqual(listLivingSingle(indis), ['I1'])

    def test3(self):
        indis = {
        'I1': {
            'Name': 'I1',
            'Alive': True,
            'Spouse': 'Blah'
        },
        'I2': {
            'Name': 'I2',
            'Alive': False,
            'Spouse': 'NA'
        },
        'I3': {
            'Name': 'I3',
            'Alive': False,
            'Spouse': 'NA'
        }}
        self.assertEqual(listLivingSingle(indis), [])

if __name__ == '__main__':
    unittest.main()
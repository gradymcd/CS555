#US12: Parents not too old
#Mother should be less than 60 years older than her children and father should be less than 80 years older than his children

import unittest
import copy

def ParentsNotTooOld(indis, fams):
	res = True
	s = {}
	for fam in fams.values():
		s[(fam['Husband ID'], fam['Wife ID'])] = fam['Children']
	for k,v in s.items():
		h, w = k
		for c in v:
			a = indis[c]['Age']
			if(indis[h]['Age'] >= 80 + a or indis[w]['Age'] >= 60 + a):
				print('Error US12: Parent of ' + indis[c]['Name'] + ' is too old')
				res = False
				
	return res
	
class TestUS12(unittest.TestCase):
	indis = {
		'I1': {
			'Name': 'I1',
			'Age': 30
		},
		'I2': {
			'Name': 'I2',
			'Age': 30
		},
		'I3': {
			'Name': 'I3',
			'Age': 0
		},
		'I4': {
			'Name': 'I4',
			'Age': 1
		},
	}
	fams = {
		'F1': {
			'Husband ID': 'I1',
			'Wife ID': 'I2',
			'Children': ['I3', 'I4']
		},
	}
	def test01(self):
		print('test01:')
		self.assertTrue(ParentsNotTooOld(self.indis, self.fams))
	def test02(self):
		print('test02:')
		indis = copy.deepcopy(self.indis)
		indis['I1']['Age'] = 81
		self.assertFalse(ParentsNotTooOld(indis, self.fams))
	def test03(self):
		print('test03:')
		indis = copy.deepcopy(self.indis)
		indis['I2']['Age'] = 61
		self.assertFalse(ParentsNotTooOld(indis, self.fams))

		
if __name__ == '__main__':
    unittest.main()
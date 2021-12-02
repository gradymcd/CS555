#US08 - Birth before marriage of parents
#Children should be born after marriage of parents (and not more than 9 months after their divorce)

from util import datify
from dateutil.relativedelta import relativedelta
import unittest
import copy

def NoBirthBeforeParentsMarried(indis, fams):
	res = True
	mdates = {}
	ddates = {}
	for fam in fams.values():
		for cid in fam['Children']:
			m = fam['Married'] 
			d = fam['Divorced']
			if m != 'NA':
				mdates[cid] = datify(m)
			if d != 'NA':
				ddates[cid] = datify(d)
	for id, indi in indis.items():
		bd = datify(indi['Birthday'])
		if id in mdates:
			if bd < mdates[id]:
				print('Error US08: ' + indis[id]['Name'] + ' was born before marriage of parents')
				res = False
		if id in ddates:
			if bd > ddates[id] + relativedelta(months=9):
				print('Error US08: ' + indis[id]['Name'] + ' was born more than 9 months after divorce of parents')
				res = False
	return res
	
class TestUS08(unittest.TestCase):
	indis = {
		'I1': {
			'Name': 'I1',
			'Birthday': '2021-01-01'
		},
		'I2': {
			'Name': 'I2',
			'Birthday': '2021-01-01'
		}
	}
	fams = {
		'F1': {
			'Husband ID': 'I2',
			'Wife ID': 'I3',
			'Children': ['I1', 'I2'],
			'Married': '2020-01-01',
			'Divorced': '2021-02-01'
		}
	}
	def test01(self):
		print('test01:')
		self.assertTrue(NoBirthBeforeParentsMarried(self.indis, self.fams))
	def test02(self):
		print('test02:')
		fams = copy.deepcopy(self.fams)
		fams['F1']['Married'] = '2021-01-02'
		self.assertFalse(NoBirthBeforeParentsMarried(self.indis, fams))
	def test03(self):
		print('test03:')
		fams = copy.deepcopy(self.fams)
		fams['F1']['Divorced'] = '2020-01-01'
		self.assertFalse(NoBirthBeforeParentsMarried(self.indis, fams))
	def test04(self):
		print('test04:')
		indis = copy.deepcopy(self.indis)
		indis['I2']['Birthday'] = '2019-01-01'
		self.assertFalse(NoBirthBeforeParentsMarried(indis, self.fams))

		
if __name__ == '__main__':
    unittest.main()
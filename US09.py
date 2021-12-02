#US09 - Birth before death of parents
#Child should be born before death of mother and before 9 months after death of father

from util import datify
from datetime import datetime
from dateutil.relativedelta import relativedelta
import unittest
import copy


def BirthBeforeDeathOfParents(indis, fams):
	res = True
	ddates = {}
	for fam in fams.values():
		h = fam['Husband ID']
		w = fam['Wife ID']
		for cid in fam['Children']:
			ddates[cid] = [datify(indis[h]['Death']), datify(indis[w]['Death'])]
	for id, indi in indis.items():
		if id in ddates:
			bd = datify(indi['Birthday'])
			fd = ddates[id][0]
			md = ddates[id][1]
			if fd != None and bd > fd + relativedelta(months=9):
				print('Error US09: ' + indis[id]['Name'] + ' was born more than 9 months after death of father')
				res = False
			if md != None and bd > md:
				print('Error US09: ' + indis[id]['Name'] + ' was born after death of mother')
				res = False
	return res
	
class TestUS09(unittest.TestCase):
	indis = {
		'I1': {
			'Name': 'I1',
			'Birthday': '2020-01-01'
		},
		'I2': {
			'Name': 'I2',
			'Death': '2021-01-01'
		},
		'I3': {
			'Name': 'I2',
			'Death': '2021-01-01'
		},
		'I4': {
			'Name': 'I2',
			'Birthday': '2020-01-01'
		}
	}
	fams = {
		'F1': {
			'Husband ID': 'I2',
			'Wife ID': 'I3',
			'Children': ['I1', 'I4']
		}
	}
	def test01(self):
		print('test01:')
		self.assertTrue(BirthBeforeDeathOfParents(self.indis, self.fams))
	def test02(self):
		print('\ntest02:')
		indis = copy.deepcopy(self.indis)
		indis['I1']['Birthday'] = '2022-01-01'
		self.assertFalse(BirthBeforeDeathOfParents(indis, self.fams))
	def test03(self):
		print('\ntest03:')
		indis = copy.deepcopy(self.indis)
		indis['I2']['Death'] = '2019-03-01'
		self.assertFalse(BirthBeforeDeathOfParents(indis, self.fams))
	def test04(self):
		print('\ntest04:')
		indis = copy.deepcopy(self.indis)
		indis['I3']['Death'] = '2019-12-31'
		self.assertFalse(BirthBeforeDeathOfParents(indis, self.fams))
	def test05(self):
		print('\ntest05:')
		indis = copy.deepcopy(self.indis)
		indis['I4']['Birthday'] = '2021-01-02'
		self.assertFalse(BirthBeforeDeathOfParents(indis, self.fams))
		
if __name__ == '__main__':
    unittest.main()
#US11
import unittest
import copy

def CheckBigamy(indis, fams):
	def helper(m):
		for k, v in m.items():
			if(len(v) > 1):
				numAlive = 0
				for s in v:
					if(indis[s]['Alive']):
						numAlive+=1
					if(numAlive > 1):
						print('Error US11: ' + indis[k]['Name'] + ' is married to multiple spouses')
						return False
		return True
	res = True
	hm = {}
	wm = {}
	for fam in fams.values():
		hid = fam['Husband ID']
		wid = fam['Wife ID']
		if(hid not in hm):
			hm[hid] = []
		if(wid not in wm):
			wm[wid] = []
		hm[hid].append(wid)
		wm[wid].append(hid)
	if(not (helper(hm) and helper(wm))):
		res = False
	return res
		
class TestUS11(unittest.TestCase):
	indis = {
		'I1': {
			'Name': 'I1',
			'Alive': True
		},
		'I2': {
			'Name': 'I2',
			'Alive': True
		},
		'I3': {
			'Name': 'I3',
			'Alive': True
		}
	}
	fams = {
		'F1': {
			'Husband ID': 'I1',
			'Wife ID': 'I2',
		},
		'F2': {
			'Husband ID': 'I1',
			'Wife ID': 'I3',
		}
	}
	def test01(self):
		print('test01:')
		self.assertFalse(CheckBigamy(self.indis, self.fams))
	def test02(self):
		print('test02:')
		fams = copy.deepcopy(self.fams)
		del fams['F2']
		self.assertTrue(CheckBigamy(self.indis, fams))
	def test03(self):
		print('test03:')
		indis = copy.deepcopy(self.indis)
		indis['I3']['Alive'] = False
		self.assertTrue(CheckBigamy(indis, self.fams))

		
if __name__ == '__main__':
    unittest.main()
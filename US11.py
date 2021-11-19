#US11

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
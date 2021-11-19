#US12: Parents not too old
#Mother should be less than 60 years older than her children and father should be less than 80 years older than his children

def ParentsTooOld(indis, fams):
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
	

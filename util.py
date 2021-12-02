from datetime import datetime

def datify(s):
	if s == 'NA':
		return None
	return datetime.strptime(s, '%Y-%m-%d').date()
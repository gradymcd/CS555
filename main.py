from datetime import datetime
from prettytable import PrettyTable
from dateutil.relativedelta import relativedelta

TagLevels = {
	"INDI": 0,
	"NAME": 1,
	"SEX":  1,
	"BIRT": 1,
	"DEAT": 1,
	"FAMC": 1,
	"FAMS": 1,
	"FAM":  0,
	"MARR": 1,
	"HUSB": 1,
	"WIFE": 1,
	"CHIL": 1,
	"DIV":  1,
	"DATE": 2,
	"HEAD": 0,
	"TRLR": 0,
	"NOTE": 0
}

def checkGed(filePath, debug=False):
	line = ''
	lineI = 0
	level = ''
	tag = ''
	valid = ''
	args = []
	indis = {}
	fams = {}
	curID = ""
	dateType = ""
	alive = True
	type = None
	

	def printLine():
		print(level + '|' + tag + '|' + valid + '|', end='')
		for arg in args:
			print(arg, end=' ')
		print()
		
	file = open(filePath, 'r')
	res = ''
	lines = file.readlines()
	areErrors = False

	for line in lines:
		lineI += 1
		line = line.replace('\n', ' ')
		
		elems = line.split(' ')
		level = elems[0]
		if("INDI" in elems or "FAM" in elems):
			tag = elems[2]
			args = [elems[1]]
			curID = args[0]
			if("INDI" in elems):
				indis[curID] = {}
				alive = True
				type = 'I'
			if('FAM' in elems):
				type = 'F'
				fams[curID] = {}
				married = False
				divorced = False
				children = []
		else:
			tag = elems[1]
			args = elems[2:]  
		valid = 'N'
		if(tag in TagLevels.keys()):
			valid = 'Y'
		
		date = datetime.now()
		
		if(tag == 'DATE'):
			date = datetime.strptime(args[0] + args[1] + args[2], '%d%b%Y')
			if(date > datetime.now()):
				res += 'ERROR US01 on line ' + str(lineI) + ': Dates (birth, marriage, divorce, death) should not be after the current date'
				if(debug):
					printLine()
				areErrors = True
			
		if(type == 'I'):
			if(tag == 'NAME'):
				indis[curID]['Name'] = args[0] + " " + args[1]
			if(tag == 'SEX'):
				indis[curID]['Gender'] = args[0]
			if(tag == 'BIRT'):
				dateType = 'BIRT'
			if(dateType == 'BIRT' and tag == 'DATE'):
				indis[curID]['Birthday'] = date.strftime("%Y-%m-%d")
				indis[curID]['Age'] = relativedelta(datetime.now(), date).years
			if(tag == 'DEAT'):
				if args[0] == 'Y':
					alive = False
				dateType = 'DEAT'
			indis[curID]['Alive'] = alive
			if(alive):
				indis[curID]['Death'] = 'NA'
			if(not(alive) and tag == 'DATE'):
				indis[curID]['Death'] = date.strftime("%Y-%m-%d")
			indis[curID]['Spouse'] = 'NA'
			indis[curID]['Child'] = 'NA'
		if(type == 'F'):
			if(tag == 'MARR'):
				fams[curID]['Married'] = 'NA'
				married = True
			if(married and tag == 'DATE'):
				fams[curID]['Married'] = date.strftime("%Y-%m-%d")
			if(tag == 'DIV'):
				fams[curID]['Divorced'] = 'NA'
				divorced = True
			if(divorced and tag == 'DATE'):
				fams[curID]['Divorced'] = date.strftime("%Y-%m-%d")
			if(tag == 'HUSB'):
				fams[curID]['Husband ID'] = args[0]
				fams[curID]['Husband Name'] = indis[args[0]]['Name']
				
			if(tag == 'WIFE'):
				fams[curID]['Wife ID'] = args[0]
				fams[curID]['Wife Name'] = indis[args[0]]['Name']
			if(tag == 'CHIL'):
				children.append(args[0])
			fams[curID]['Children'] = children
			if(not married):
				fams[curID]['Married'] = 'NA'
			if(not divorced):
				fams[curID]['Divorced'] = 'NA'
			
		
	famTable = PrettyTable()
	famTable.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
	for key, val in fams.items():
		famTable.add_row([key, val['Married'], val['Divorced'], val['Husband ID'], val['Husband Name'], val['Wife ID'], val['Wife Name'], val['Children']])
		indis[val['Husband ID']]['Spouse'] = key
		indis[val['Wife ID']]['Spouse'] = key
		for childID in val['Children']:
			indis[childID]['Child'] = key
		
		
	indiTable = PrettyTable()
	indiTable.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
	for key, val in indis.items():
		indiTable.add_row([key, val['Name'], val['Gender'], val['Birthday'], val['Age'], val['Alive'], val['Death'], val['Child'], val['Spouse']])

	res += indiTable.get_string() + '\n' + famTable.get_string()

	file.close()
	return res

if __name__ == '__main__':
	file = input('File: ')
	print(checkGed(file))

from datetime import datetime
from prettytable import PrettyTable
from dateutil.relativedelta import relativedelta
import US23, US38

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
	individualIds = []
	familyIds = []
	siblings = {}
	marriages = []
	
	if(not US23.UniqueNameBirthdate(filePath)):
		print('Error US23: No more than one individual with the same name and birth date should appear in a GEDCOM file')
		
	file = open(filePath, 'r')
	res = ''
	lines = file.readlines()
	
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
				if(curID in individualIds):
					print( 'Error US22: Duplicate individual ID ({}) on line {}.'.format(curID, lineI))
				individualIds.append(curID)
				indis[curID] = {}
				alive = True
				type = 'I'
				siblings[curID] = []
			if('FAM' in elems):
				if(curID in familyIds):
					print('Error US22: Duplicate family ID ({}) on line {}.'.format(curID, lineI))
				familyIds.append(curID)
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
			try:
				date = datetime.strptime(args[0] + args[1] + args[2], '%d%b%Y')
			except ValueError:
				print('ERROR: US42: Invalid date on line {}.\n'.format(lineI))
				date = None
				break
			if(date > datetime.now()):
				res += 'ERROR US01 on line ' + str(lineI) + ': Dates (birth, marriage, divorce, death) should not be after the current date\n'
			
		if(type == 'I'):
			if(tag == 'NAME'):
				indis[curID]['Name'] = args[0] + " " + args[1]
			if(tag == 'SEX'):
				indis[curID]['Gender'] = args[0]
			if(tag == 'BIRT'):
				dateType = 'BIRT'
				indis[curID]['Birthday'] = 'N/A'
				indis[curID]['Age'] = 'N/A'
			if(dateType == 'BIRT' and tag == 'DATE'):
				if(date == None):
					indis[curID]['Birthday'] = 'N/A'
					indis[curID]['Age'] = 'N/A'
				else:	
					indis[curID]['Birthday'] = date.strftime("%Y-%m-%d")
					indis[curID]['Age'] = relativedelta(datetime.now(), date).years
					if (indis[curID]['Age']) >= 150:
						print("Error US07: on line " + str(lineI) + ", there should not be a person alive after 150 years")
                
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
				marriages.append(args[0])
			if(tag == 'WIFE'):
				fams[curID]['Wife ID'] = args[0]
				fams[curID]['Wife Name'] = indis[args[0]]['Name']
				marriages.append(args[0])
			if(tag == 'CHIL'):
				children.append(args[0])
				siblings[fams[curID]['Wife ID']].append(args[0])
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
		
	upcomingBirthdays = []
	indiTable = PrettyTable()
	indiTable.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
	for key, val in indis.items():
		indiTable.add_row([key, val['Name'], val['Gender'], val['Birthday'], val['Age'], val['Alive'], val['Death'], val['Child'], val['Spouse']])
		if (val['Alive'] and US38.checkUpcomingBirthday(val['Birthday'])):
			upcomingBirthdays.append(val['Name'])
			
	
	res += indiTable.get_string() + '\n' + famTable.get_string() + '\n'
	
	res += 'Siblings:\n'
	for p, cs in siblings.items():
		if(cs != [] and len(cs) > 1):
			print(cs, len(cs))
			for i in range(len(cs)):
				cs[i] = indis[cs[i]]
				print(cs[i])
			for v in sorted(cs, key=lambda x : x['Age'], reverse=True):
				res += v['Name'] + '(' + str(v['Age']) + ')   '
			res += '\n'
				
	res += '\nLiving married: \n'
	for id in marriages:
		if(indis[id]['Alive']):
			res += indis[id]['Name'] + '\n'
			
	if not upcomingBirthdays:
		res += '\n' + "No upcoming birthdays"
	else:
		res += '\n' + "Upcoming birthdays: "
		for n in upcomingBirthdays:
			res += n + " "

	file.close()
	return res

if __name__ == '__main__':
	file = input('File: ')
	print(checkGed(file))
	input()

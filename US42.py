from datetime import datetime
def rejectInvalidDates(input):
    lines = input.splitlines()

    for lineCount, line in enumerate(lines):
        line = line.strip()

        l = line.split(' ', 2)

        level = l[0]
        tag = l[1]
        try: 
            args = l[2]
        except: 
            args = ""

        if tag == 'DATE':
            date = args.split(' ', 2)
            try:
                valid = datetime.strptime(date[0] + date[1] + date[2], '%d%b%Y')
            except ValueError:
                print('Error US42: Invalid date on line {}. ({})\n'.format(lineCount, args))

    return
import unittest

# US22
def uniqueIDs(input):
    lines = input.splitlines()

    individualIds = []
    familyIds = []

    for lineCount, line in enumerate(lines):
        line = line.strip()

        l = line.split(' ', 2)

        level = l[0]
        tag = l[1]
        try: 
            args = l[2]
        except: 
            args = ""

        args, tag = tag, args

        if tag == 'INDI':
            if individualIds.count(args) == 1:
                return(printErrorMessageUS22(args, lineCount, 'individual'))
            else:
                individualIds.append(args)
        elif tag == 'FAM':
            if familyIds.count(args) == 1:
                return(printErrorMessageUS22(args, lineCount, 'family'))
            else:
                familyIds.append(args)

    return "OK"

def printErrorMessageUS22(id, lineCount, idType):
    return('Error US22: Duplicate {} ID ({}) on line {}.\n'.format(idType, id, lineCount))

class TestUS22(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(uniqueIDs(""), "OK")

    def test_pass1(self):
        self.assertEqual(uniqueIDs(
            "0 test1 INDI\n0 test2 INDI"), 
        "OK")

    def test_fail1(self):
        self.assertEqual(uniqueIDs(
            "0 test1 INDI\n0 test1 INDI"),
        "Error US22: Duplicate individual ID (test1) on line 1.\n")

    def test_pass2(self):
        self.assertEqual(uniqueIDs(
            "0 test1 FAM\n0 test2 FAM"),
        "OK")

    def test_fail2(self):
        self.assertEqual(uniqueIDs(
            "0 test1 FAM\n0 test1 FAM"),
        "Error US22: Duplicate family ID (test1) on line 1.\n")

    def test_pass3(self):
        self.assertEqual(uniqueIDs(
            "0 test1 FAM\n0 test1 INDI"),
        "OK")

    def test_fail3(self):
        self.assertEqual(uniqueIDs(
            "0 test1 FAM\n0 test1 INDI\n0 test1 FAM"),
        "Error US22: Duplicate family ID (test1) on line 2.\n")

    def test_fail4(self):
        self.assertEqual(uniqueIDs(
            "0 test1 FAM\n0 test1 INDI\n0 test1 FAM\n0 test1 INDI"),
        "Error US22: Duplicate family ID (test1) on line 2.\n")

    def test_fail5(self):
        self.assertEqual(uniqueIDs(
            "0 test1 FAM\n0 test1 INDI\n0 test2 FAM\n0 test1 INDI"),
        "Error US22: Duplicate individual ID (test1) on line 3.\n")

if __name__ == '__main__':
    unittest.main()
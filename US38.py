import unittest
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

# US38
def checkUpcomingBirthday(datestring):
    birthdate = datetime.strptime(datestring, "%Y-%m-%d")
    try:
        birthdate = date(datetime.now().year, birthdate.month, birthdate.day)
    except:
        birthdate = date(datetime.now().year, birthdate.month, birthdate.day-1)
    d = relativedelta(birthdate, datetime.now()).days
    m = relativedelta(birthdate, datetime.now()).months
    if 0 <= d <= 30 and m == 0:
        return True
    return False


class TestUS38(unittest.TestCase):
    def test_true1(self):
        self.assertEqual(checkUpcomingBirthday("2021-12-02"), True)

    def test_true2(self):
        self.assertEqual(checkUpcomingBirthday("2020-12-02"), True)

    def test_false1(self):
        self.assertEqual(checkUpcomingBirthday("2021-11-07"), False)

    def test_false2(self):
        self.assertEqual(checkUpcomingBirthday("2021-12-15"), False)

if __name__ == '__main__':
    unittest.main()
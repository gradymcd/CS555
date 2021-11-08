import unittest
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

# US38
def checkUpcomingBirthday(datestring):
    birthdate = datetime.strptime(datestring, "%Y-%m-%d")
    d = relativedelta(birthdate, datetime.now()).days
    m = relativedelta(birthdate, datetime.now()).months
    y = relativedelta(birthdate, datetime.now()).years
    if d <= 30 and m == 0 and y == 0:
        return True
    return False


class TestUS38(unittest.TestCase):
    def test_true(self):
        self.assertEqual(checkUpcomingBirthday("2021-12-02"), True)

    def test_false(self):
        self.assertEqual(checkUpcomingBirthday("2022-11-11"), False)

if __name__ == '__main__':
    unittest.main()
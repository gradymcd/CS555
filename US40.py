import unittest

# US40
# This was already implemented in the code,
# but this serves as testing the code that we use for line counts.
def lineCount(input):
    lines = input.splitlines()
    for lineCount, line in enumerate(lines):
        if line == "ERROR":
            return lineCount
    return -1

class TestUS40(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(lineCount(""), -1)

    def test_1(self):
        self.assertEqual(lineCount("ERROR"), 0)

    def test_2(self):
        self.assertEqual(lineCount("\nERROR"), 1)

    def test_3(self):
        self.assertEqual(lineCount("\n\nERROR"), 2)

if __name__ == '__main__':
    unittest.main()
import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 3)), 6, "Should be 6")

class TestDivision(unittest.TestCase):

    def test_division(self):
        self.assertEqual(10/2, 5)

    def test_division_divmod(self):
        self.assertEqual(divmod(20,5), (4,0))

if __name__ == '__main__':
    TestSum()
    TestDivision()
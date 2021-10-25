from O_logn import BinarySearch

import unittest


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.bs = BinarySearch()
        self.test_array = [2, 4, 5, 5, 7, 16, 23, 29, 32, 47]

    def test1_is_number_in(self):
        self.assertTrue(self.bs.is_number_in(5, self.test_array))

    def test2_is_number_in(self):
        self.assertFalse(self.bs.is_number_in(15, self.test_array))

    def test3_is_number_in(self):
        self.assertFalse(self.bs.is_number_in(25, self.test_array))


if __name__ == '__main__':
    unittest.main()

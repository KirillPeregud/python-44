from O_nlogn import CheckDublicate

import unittest


class TestCheckDublicate(unittest.TestCase):

    def setUp(self):
        self.cd = CheckDublicate()
        self.test_array = [2, 4, 5, 5, 5, 7, 16, 23, 23, 23, 29, 32, 47]

    def test1_check(self):
        self.assertEqual(self.cd.check(self.test_array), [5, 23])

    def test2_check(self):
        self.assertNotEqual(self.cd.check(self.test_array), [4, 16, 29])

    def test3_check(self):
        self.assertNotEqual(self.cd.check(self.test_array), [5, 5, 23])


if __name__ == '__main__':
    unittest.main()

import unittest

from kmp import find_match, build_prefix_table


class MyTestCase(unittest.TestCase):
    def test_find_match(self):
        self.assertEqual(find_match('zxcvbnm', 'vbn'), True)

    def test_build_prefix_table(self):
        self.assertEqual(build_prefix_table("kbbkkbbk"), [0, 0, 0, 1, 1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()

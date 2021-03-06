import unittest
import example


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(example.add(1, 2), 3)

    def test_subtract_1(self):
        self.assertEqual(example.subtract(1, 1), 0)

    def test_multiply_2(self):
        self.assertEqual(example.multiply(2, 2), 4)

    def test_division_2(self):
        self.assertEqual(example.division(4, 2), 2)


if __name__ == '__main__':
    unittest.main()

import unittest

from src.mathematics import Mathematics


class TestMathematics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = Mathematics()

    def test_sum(self):
        data = [
            ("positive", 2, 2, 4),
            ("zero", -2, 2, 0),
            ("negative", -2, -2, -4),
        ]
        for i in range(len(data)):
            with self.subTest(data[i][0]):
                self.assertEqual(self.m.sum(data[i][1], data[i][2]), data[i][3])

    def test_divide_exception(self):
        self.assertRaises(ZeroDivisionError, lambda: self.m.divide(3, 0))

    def test_divide(self):
        data = [
            ("positive", 2, 2, 1),
            ("zero", 0, 2, 0),
            ("negative", -2, 2, -1),
            ("fraction", 2, 4, 0.5)
        ]
        for i in range(len(data)):
            with self.subTest(data[i][0]):
                self.assertEqual(self.m.divide(data[i][1], data[i][2]), data[i][3])


if __name__ == "__main__":
    unittest.main()

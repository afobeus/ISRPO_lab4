import unittest
from geometric_lib_new.square import area, perimeter


class TestSquare(unittest.TestCase):
    def test_area_positive_side(self):
        self.assertEqual(area(1), 1)
        self.assertEqual(area(2.5), 2.5 * 2.5)
        self.assertEqual(area(100), 100 * 100)

    def test_area_zero_side(self):
        self.assertEqual(area(0), 0)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_area_large_side(self):
        self.assertEqual(area(1e6), 1e6 ** 2)

    def test_area_invalid_type(self):
        with self.assertRaises(TypeError):
            area("side")

    def test_perimeter_positive_side(self):
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(2.5), 4 * 2.5)
        self.assertEqual(perimeter(100), 4 * 100)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-1)

    def test_perimeter_large_side(self):
        self.assertEqual(perimeter(1e6), 4 * 1e6)

    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            perimeter("side")


if __name__ == '__main__':
    unittest.main()

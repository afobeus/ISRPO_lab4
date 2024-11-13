import unittest
import math
from geometric_lib_new.circle import area, perimeter


class TestCircle(unittest.TestCase):
    def test_area_positive_radius(self):
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(0.5), math.pi * 0.5 * 0.5)
        self.assertAlmostEqual(area(2.5), math.pi * 2.5 * 2.5)

    def test_area_zero_radius(self):
        self.assertAlmostEqual(area(0), 0)

    def test_area_negative_radius(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_area_large_radius(self):
        self.assertAlmostEqual(area(1e6), math.pi * 1e6 ** 2)

    def test_area_invalid_type(self):
        with self.assertRaises(TypeError):
            area("radius")

    def test_perimeter_positive_radius(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter(0.5), 2 * math.pi * 0.5)
        self.assertAlmostEqual(perimeter(2.5), 2 * math.pi * 2.5)

    def test_perimeter_zero_radius(self):
        self.assertAlmostEqual(perimeter(0), 0)

    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            perimeter(-1)

    def test_perimeter_large_radius(self):
        self.assertAlmostEqual(perimeter(1e6), 2 * math.pi * 1e6)

    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            perimeter("radius")


if __name__ == '__main__':
    unittest.main()

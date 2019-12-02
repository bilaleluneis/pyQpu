from unittest import TestCase
from video_core_iv import Vector, VectorSizeError, VectorTypeError

__author__ = "Bilal El Uneis"
__since__ = "Nov 2019"
__email__ = "bilaleluneis@gmail.com"


class TestVector(TestCase):

    def setUp(self) -> None:
        pass

    def test_valid(self) -> None:
        Vector([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

    def test_invalid_length(self) -> None:
        with self.assertRaises(VectorSizeError):
            Vector([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

    def test_invalid_boolean_type(self) -> None:
        with self.assertRaises(VectorTypeError):
            Vector([True, False, True, True, True, True, True, True,
                    True, False, True, True, True, True, True, True])

    def test_invalid_mixed_type(self) -> None:
        with self.assertRaises(VectorTypeError):
            Vector([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 2.4, 2.5])

    def test_add(self) -> None:
        v1 = Vector([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
        v2 = Vector([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
        v3 = v1 + v2
        self.assertEqual(v3.value, [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])

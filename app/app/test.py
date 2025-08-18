from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):

    def test_add(self):
        """Test the add function"""
        res = calc.add(3, 5)
        self.assertEqual(res, 8)

    def test_subtract(self):
        """Test the subtract function"""
        res = calc.subtract(10, 5)
        self.assertEqual(res, 5)

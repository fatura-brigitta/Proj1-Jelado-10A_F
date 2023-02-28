from unittest import TestCase
from Jel import Jel


class TestJeladás(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.jel1: Jel = Jel('3 11 19 122 644')
        cls.jel2: Jel = Jel('16 42 36 76 656')

    def test_x_kord(self):
        self.assertEqual(self.jel1.x_kord, 122)
        self.assertEqual(self.jel2.x_kord, 76)

    def test_y_kord(self):
        self.assertEqual(self.jel1.y_kord, 644)
        self.assertEqual(self.jel2.y_kord, 656)

    def test_óra(self):
        self.assertEqual(self.jel1.óra, 3)
        self.assertEqual(self.jel2.óra, 16)

    def test_perc(self):
        self.assertEqual(self.jel1.perc, 11)
        self.assertEqual(self.jel2.perc, 42)

    def test_másodperc(self):
        self.assertEqual(self.jel1.másodperc, 19)
        self.assertEqual(self.jel2.másodperc, 36)

    def test_idő_mspercben(self):
        self.assertEqual(self.jel1.idő_mspercben, 11479)
        self.assertEqual(self.jel2.idő_mspercben, 60156)

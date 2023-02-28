import filecmp
from unittest import TestCase
from Megoldas import Megoldas


class TestMegoldás(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.megoldás1: Megoldas = Megoldas('jel.txt')

        cls.sor1: int = 1
        cls.sor2: int = 2
        cls.sor12: int = 12
        cls.sor13: int = 13
        cls.sor52: int = 52
        cls.sor53: int = 53

        cls.sor1_2 = cls.megoldás1._jelek[0]
        cls.sor2_2 = cls.megoldás1._jelek[1]
        cls.sor12_2 = cls.megoldás1._jelek[11]
        cls.sor13_2 = cls.megoldás1._jelek[12]
        cls.sor52_2 = cls.megoldás1._jelek[51]
        cls.sor53_2 = cls.megoldás1._jelek[52]

    def test_első_utolsó_között_mspben(self):
        self.assertEqual(self.megoldás1.első_utolsó_között_mspben, 67960)

    def test_mspből_óra(self):
        self.assertEqual(self.megoldás1.mspből_óra, 18)

    def test_maradék_perc(self):
        self.assertEqual(self.megoldás1.maradék_perc, 52)

    def test_maradék_msperc(self):
        self.assertEqual(self.megoldás1.maradék_msperc, 40)

    def test_bal_also_x_keres(self):
        self.assertEqual(self.megoldás1.bal_also_x_keres, 4)

    def test_bal_also_y_keres(self):
        self.assertEqual(self.megoldás1.bal_also_y_keres, 639)

    def test_jobb_felso_x_keres(self):
        self.assertEqual(self.megoldás1.jobb_felso_x_keres, 147)

    def test_jobb_felso_y_keres(self):
        self.assertEqual(self.megoldás1.jobb_felso_y_keres, 727)

    def test_jobb_táv_pontok_közt(self):
        self.assertEqual(self.megoldás1.táv_pontok_közt, 2007.677)

    def test_x_kordináta_keres(self):
        self.assertEqual(self.megoldás1.x_kordináta_keres(self.sor1), 122)
        self.assertEqual(self.megoldás1.x_kordináta_keres(self.sor12), 101)
        self.assertEqual(self.megoldás1.x_kordináta_keres(self.sor52), 87)

    def test_y_kordináta_keres(self):
        self.assertEqual(self.megoldás1.y_kordináta_keres(self.sor1), 644)
        self.assertEqual(self.megoldás1.y_kordináta_keres(self.sor12), 669)
        self.assertEqual(self.megoldás1.y_kordináta_keres(self.sor52), 653)

    def test_eltelt(self):
        self.assertEqual(self.megoldás1.eltelt(self.sor1, self.sor2), 1)
        self.assertEqual(self.megoldás1.eltelt(self.sor12, self.sor13), 1)
        self.assertEqual(self.megoldás1.eltelt(self.sor52, self.sor53), 1)

    def test_távolság_kimaradtakhoz(self):
        self.assertEqual(self.megoldás1.távolság_kimaradtakhoz(self.sor1_2, self.sor2_2), 2)
        self.assertEqual(self.megoldás1.távolság_kimaradtakhoz(self.sor12_2, self.sor13_2), 8)
        self.assertEqual(self.megoldás1.távolság_kimaradtakhoz(self.sor52_2, self.sor53_2), 7)

    def test_kimaradtak_ido_szerint(self):
        self.assertEqual(self.megoldás1.kimaradtak_ido_szerint(self.sor1_2.idő_mspercben, self.sor2_2.idő_mspercben), 0)
        self.assertEqual(self.megoldás1.kimaradtak_ido_szerint(self.sor12_2.idő_mspercben, self.sor13_2.idő_mspercben), 0)
        self.assertEqual(self.megoldás1.kimaradtak_ido_szerint(self.sor52_2.idő_mspercben, self.sor53_2.idő_mspercben), 0)

    def test_kimaradtak_tav_szerint(self):
        self.assertEqual(self.megoldás1.kimaradtak_tav_szerint(self.sor1_2, self.sor2_2), 0)
        self.assertEqual(self.megoldás1.kimaradtak_tav_szerint(self.sor12_2, self.sor13_2), 0)
        self.assertEqual(self.megoldás1.kimaradtak_tav_szerint(self.sor52_2, self.sor53_2), 0)

    def test_kimaradtak_kigyujtese(self):
        self.megoldás1.kimaradtak_kigyujtese('kimaradt.txt')
        self.assertTrue(filecmp.cmp('kimaradt.txt', 'kimaradt_OH.txt', shallow=False))

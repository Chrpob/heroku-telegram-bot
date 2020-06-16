import unittest
from modelos.teprosif import Teprosif, NORMAL, RIESGO, DEFICIT

class TestTeprosif(unittest.TestCase):
    def test_edad_3(self):
        normal_1 = Teprosif(3, '27.0')
        normal_2 = Teprosif(3, '23')
        normal_3 = Teprosif(3, '33')
        riesgo = Teprosif('3', '48')
        deficit = Teprosif('3', '58')
        self.assertEqual(normal_1.resultados['resultado'], NORMAL)
        self.assertEqual(normal_1.resultados['sd'], 0.0)
        self.assertEqual(normal_2.resultados['resultado'], NORMAL)
        self.assertEqual(normal_2.resultados['sd'], -0.26490066225165565)
        self.assertEqual(normal_3.resultados['resultado'], NORMAL)
        self.assertEqual(normal_3.resultados['sd'], 0.3973509933774835)
        self.assertEqual(riesgo.resultados['resultado'], RIESGO)
        self.assertEqual(riesgo.resultados['sd'], 1.390728476821192)
        self.assertEqual(deficit.resultados['resultado'], DEFICIT)
        self.assertEqual(deficit.resultados['sd'], 2.052980132450331)

    def test_edad_4(self):
        normal = Teprosif(4, '15')
        riesgo = Teprosif('4', '25')
        deficit = Teprosif('4', '38')
        self.assertEqual(normal.resultados['resultado'], NORMAL)
        self.assertEqual(riesgo.resultados['resultado'], RIESGO)
        self.assertEqual(deficit.resultados['resultado'], DEFICIT)

    def test_edad_5(self):
        normal = Teprosif(5, '12')
        riesgo = Teprosif('5', '18')
        deficit = Teprosif('5', '22')
        self.assertEqual(normal.resultados['resultado'], NORMAL)
        self.assertEqual(riesgo.resultados['resultado'], RIESGO)
        self.assertEqual(deficit.resultados['resultado'], DEFICIT)

    def test_edad_6(self):
        normal = Teprosif(6, '10')
        riesgo = Teprosif('6', '12')
        deficit = Teprosif('6', '16')
        self.assertEqual(normal.resultados['resultado'], NORMAL)
        self.assertEqual(riesgo.resultados['resultado'], RIESGO)
        self.assertEqual(deficit.resultados['resultado'], DEFICIT)


if __name__ == '__main__':
    unittest.main()

import unittest
from modelos.tecal import Tecal, VOCABULARIO, MORFOLOGIA, SINTAXIS, TOTAL, RESULTADO, NORMAL, RIESGO, DEFICIT


class TestTecal(unittest.TestCase):
    def test_edad_3(self):
        voc_normal_mor_normal_sin_normal_tot_normal     = Tecal('3', 23.6, 23.13, 5, 52.26)
        voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo     = Tecal('3', 26.6, 28.13, 6.5, 59.26)
        voc_deficit_mor_deficit_sin_deficit_tot_deficit = Tecal('3', 30.6, 33.13, 8, 66.26)
        self.assertEqual(voc_normal_mor_normal_sin_normal_tot_normal.resultados[VOCABULARIO][RESULTADO], NORMAL)
        self.assertEqual(voc_normal_mor_normal_sin_normal_tot_normal.resultados[MORFOLOGIA][RESULTADO], NORMAL)
        self.assertEqual(voc_normal_mor_normal_sin_normal_tot_normal.resultados[SINTAXIS][RESULTADO], NORMAL)
        self.assertEqual(voc_normal_mor_normal_sin_normal_tot_normal.resultados[TOTAL][RESULTADO], NORMAL)

        self.assertEqual(voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo.resultados[VOCABULARIO][RESULTADO], RIESGO)
        self.assertEqual(voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo.resultados[MORFOLOGIA][RESULTADO], RIESGO)
        self.assertEqual(voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo.resultados[SINTAXIS][RESULTADO], RIESGO)
        self.assertEqual(voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo.resultados[TOTAL][RESULTADO], RIESGO)

        self.assertEqual(voc_deficit_mor_deficit_sin_deficit_tot_deficit.resultados[VOCABULARIO][RESULTADO], DEFICIT)
        self.assertEqual(voc_deficit_mor_deficit_sin_deficit_tot_deficit.resultados[MORFOLOGIA][RESULTADO], DEFICIT)
        self.assertEqual(voc_deficit_mor_deficit_sin_deficit_tot_deficit.resultados[SINTAXIS][RESULTADO], DEFICIT)
        self.assertEqual(voc_deficit_mor_deficit_sin_deficit_tot_deficit.resultados[TOTAL][RESULTADO], DEFICIT)

    def test_edad_4(self):
        voc_normal_mor_normal_sin_normal_tot_normal     = Tecal('4', 28.4, 28.7,  5.9, 62.26)
        voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo     = Tecal('4', 35.1, 34.5,  7.7, 72.26)
        voc_deficit_mor_deficit_sin_deficit_tot_deficit = Tecal('4', 37.1, 40.13, 10.1, 84.26)
        self.assertEqual(voc_normal_mor_normal_sin_normal_tot_normal.resultados[VOCABULARIO][RESULTADO], NORMAL)
        self.assertEqual(voc_normal_mor_normal_sin_normal_tot_normal.resultados[MORFOLOGIA][RESULTADO], NORMAL)
        self.assertEqual(voc_normal_mor_normal_sin_normal_tot_normal.resultados[SINTAXIS][RESULTADO], NORMAL)
        self.assertEqual(voc_normal_mor_normal_sin_normal_tot_normal.resultados[TOTAL][RESULTADO], NORMAL)

        self.assertEqual(voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo.resultados[VOCABULARIO][RESULTADO], RIESGO)
        self.assertEqual(voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo.resultados[MORFOLOGIA][RESULTADO], RIESGO)
        self.assertEqual(voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo.resultados[SINTAXIS][RESULTADO], RIESGO)
        self.assertEqual(voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo.resultados[TOTAL][RESULTADO], RIESGO)

        self.assertEqual(voc_deficit_mor_deficit_sin_deficit_tot_deficit.resultados[VOCABULARIO][RESULTADO], DEFICIT)
        self.assertEqual(voc_deficit_mor_deficit_sin_deficit_tot_deficit.resultados[MORFOLOGIA][RESULTADO], DEFICIT)
        self.assertEqual(voc_deficit_mor_deficit_sin_deficit_tot_deficit.resultados[SINTAXIS][RESULTADO], DEFICIT)
        self.assertEqual(voc_deficit_mor_deficit_sin_deficit_tot_deficit.resultados[TOTAL][RESULTADO], DEFICIT)

    def test_edad_5(self):
        voc_normal_mor_normal_sin_normal_tot_normal     = Tecal('5', 35.7, 38.13, 9.22, 84.26)
        voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo     = Tecal('5', 38.7, 42.93, 10.8, 90.26)
        voc_deficit_mor_deficit_sin_deficit_tot_deficit = Tecal('5', 41.7, 48.13, 13.1, 99.26)
        self.assertEqual(voc_normal_mor_normal_sin_normal_tot_normal.resultados[VOCABULARIO][RESULTADO], NORMAL)
        self.assertEqual(voc_normal_mor_normal_sin_normal_tot_normal.resultados[MORFOLOGIA][RESULTADO], NORMAL)
        self.assertEqual(voc_normal_mor_normal_sin_normal_tot_normal.resultados[SINTAXIS][RESULTADO], NORMAL)
        self.assertEqual(voc_normal_mor_normal_sin_normal_tot_normal.resultados[TOTAL][RESULTADO], NORMAL)

        self.assertEqual(voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo.resultados[VOCABULARIO][RESULTADO], RIESGO)
        self.assertEqual(voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo.resultados[MORFOLOGIA][RESULTADO], RIESGO)
        self.assertEqual(voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo.resultados[SINTAXIS][RESULTADO], RIESGO)
        self.assertEqual(voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo.resultados[TOTAL][RESULTADO], RIESGO)

        self.assertEqual(voc_deficit_mor_deficit_sin_deficit_tot_deficit.resultados[VOCABULARIO][RESULTADO], DEFICIT)
        self.assertEqual(voc_deficit_mor_deficit_sin_deficit_tot_deficit.resultados[MORFOLOGIA][RESULTADO], DEFICIT)
        self.assertEqual(voc_deficit_mor_deficit_sin_deficit_tot_deficit.resultados[SINTAXIS][RESULTADO], DEFICIT)
        self.assertEqual(voc_deficit_mor_deficit_sin_deficit_tot_deficit.resultados[TOTAL][RESULTADO], DEFICIT)

    def test_edad_6(self):
        voc_normal_mor_normal_sin_normal_tot_normal     = Tecal('6', 37.6, 41.13, 9.83,  89.26)
        voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo     = Tecal('6', 40.0, 45.13, 11.83, 95.26)
        voc_deficit_mor_deficit_sin_deficit_tot_deficit = Tecal(6,   46.6, 50.13, 13.1,  103.26)
        self.assertEqual(voc_normal_mor_normal_sin_normal_tot_normal.resultados[VOCABULARIO][RESULTADO], NORMAL)
        self.assertEqual(voc_normal_mor_normal_sin_normal_tot_normal.resultados[MORFOLOGIA][RESULTADO], NORMAL)
        self.assertEqual(voc_normal_mor_normal_sin_normal_tot_normal.resultados[SINTAXIS][RESULTADO], NORMAL)
        self.assertEqual(voc_normal_mor_normal_sin_normal_tot_normal.resultados[TOTAL][RESULTADO], NORMAL)

        self.assertEqual(voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo.resultados[VOCABULARIO][RESULTADO], RIESGO)
        self.assertEqual(voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo.resultados[MORFOLOGIA][RESULTADO], RIESGO)
        self.assertEqual(voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo.resultados[SINTAXIS][RESULTADO], RIESGO)
        self.assertEqual(voc_riesgo_mor_riesgo_sin_riesgo_tot_riesgo.resultados[TOTAL][RESULTADO], RIESGO)

        self.assertEqual(voc_deficit_mor_deficit_sin_deficit_tot_deficit.resultados[VOCABULARIO][RESULTADO], DEFICIT)
        self.assertEqual(voc_deficit_mor_deficit_sin_deficit_tot_deficit.resultados[MORFOLOGIA][RESULTADO], DEFICIT)
        self.assertEqual(voc_deficit_mor_deficit_sin_deficit_tot_deficit.resultados[SINTAXIS][RESULTADO], DEFICIT)
        self.assertEqual(voc_deficit_mor_deficit_sin_deficit_tot_deficit.resultados[TOTAL][RESULTADO], DEFICIT)


if __name__ == '__main__':
    unittest.main()

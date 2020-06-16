import unittest
from modelos.edna import Edna, DESEMPENO_NARRATIVO, COMPRENSION_DISCURSO_NARRATIVO

class TestEdna(unittest.TestCase):
    def test_edad_4(self):
        # dn: 2, 4, 9, 12, 14
        # cdn: 12, 19, 26, 30, 34
        dn_deficit_y_cdn_deficit = Edna('4', '1', '7')
        dn_deficit_y_cdn_normal_bajo = Edna('4', '2', '15')
        self.assertEqual(dn_deficit_y_cdn_deficit.resultados[DESEMPENO_NARRATIVO]['resultado'], 'Deficit')
        self.assertEqual(dn_deficit_y_cdn_deficit.resultados[DESEMPENO_NARRATIVO]['percentil'], 'Menor a p10')
        self.assertEqual(dn_deficit_y_cdn_deficit.resultados[COMPRENSION_DISCURSO_NARRATIVO]['resultado'], 'Deficit')
        self.assertEqual(dn_deficit_y_cdn_deficit.resultados[COMPRENSION_DISCURSO_NARRATIVO]['percentil'], 'Menor a p10')

        self.assertEqual(dn_deficit_y_cdn_normal_bajo.resultados[DESEMPENO_NARRATIVO]['resultado'], 'Deficit')
        self.assertEqual(dn_deficit_y_cdn_normal_bajo.resultados[DESEMPENO_NARRATIVO]['percentil'], 'Igual a p10')
        self.assertEqual(dn_deficit_y_cdn_normal_bajo.resultados[COMPRENSION_DISCURSO_NARRATIVO]['resultado'], 'Normal bajo')
        self.assertEqual(dn_deficit_y_cdn_normal_bajo.resultados[COMPRENSION_DISCURSO_NARRATIVO]['percentil'], 'Menor a p25')
        # dn_normal_bajo_cdn_normal_bajo = Edna('4', '')

    def test_edad_5(self):
        # dn: 2, 6, 11, 16, 18
        # cdn: 12, 19, 26, 30, 34
        dn_normal_bajo_y_cdn_normal_bajo = Edna('5', '5', '19')
        dn_normal_bajo_y_cdn_normal =      Edna('5', '6', '23')
        self.assertEqual(dn_normal_bajo_y_cdn_normal_bajo.resultados[DESEMPENO_NARRATIVO]['resultado'], 'Normal bajo')
        self.assertEqual(dn_normal_bajo_y_cdn_normal_bajo.resultados[DESEMPENO_NARRATIVO]['percentil'], 'Menor a p25')
        self.assertEqual(dn_normal_bajo_y_cdn_normal_bajo.resultados[COMPRENSION_DISCURSO_NARRATIVO]['resultado'], 'Normal bajo')
        self.assertEqual(dn_normal_bajo_y_cdn_normal_bajo.resultados[COMPRENSION_DISCURSO_NARRATIVO]['percentil'], 'Igual a p25')

        self.assertEqual(dn_normal_bajo_y_cdn_normal.resultados[DESEMPENO_NARRATIVO]['resultado'], 'Normal bajo')
        self.assertEqual(dn_normal_bajo_y_cdn_normal.resultados[DESEMPENO_NARRATIVO]['percentil'], 'Igual a p25')
        self.assertEqual(dn_normal_bajo_y_cdn_normal.resultados[COMPRENSION_DISCURSO_NARRATIVO]['resultado'], 'Normal')
        self.assertEqual(dn_normal_bajo_y_cdn_normal.resultados[COMPRENSION_DISCURSO_NARRATIVO]['percentil'], 'Menor a p50')
        # dn_normal_bajo_cdn_normal_bajo = Edna('4', '')


    def test_edad_6(self):
        # dn: 9, 11, 13, 17, 18
        # cdn: 19, 25, 30, 33, 35
        dn_normal_y_cdn_normal_1 = Edna('6', '12', '31')
        dn_normal_y_cdn_normal_2 = Edna('6', '13', '33')
        self.assertEqual(dn_normal_y_cdn_normal_1.resultados[DESEMPENO_NARRATIVO]['resultado'], 'Normal')
        self.assertEqual(dn_normal_y_cdn_normal_1.resultados[DESEMPENO_NARRATIVO]['percentil'], 'Menor a p50')
        self.assertEqual(dn_normal_y_cdn_normal_1.resultados[COMPRENSION_DISCURSO_NARRATIVO]['resultado'],
                         'Normal')
        self.assertEqual(dn_normal_y_cdn_normal_1.resultados[COMPRENSION_DISCURSO_NARRATIVO]['percentil'],
                         'Menor a p75')

        self.assertEqual(dn_normal_y_cdn_normal_2.resultados[DESEMPENO_NARRATIVO]['resultado'], 'Normal')
        self.assertEqual(dn_normal_y_cdn_normal_2.resultados[DESEMPENO_NARRATIVO]['percentil'], 'Igual a p50')
        self.assertEqual(dn_normal_y_cdn_normal_2.resultados[COMPRENSION_DISCURSO_NARRATIVO]['resultado'], 'Normal')
        self.assertEqual(dn_normal_y_cdn_normal_2.resultados[COMPRENSION_DISCURSO_NARRATIVO]['percentil'], 'Igual a p75')
        # dn_normal_bajo_cdn_normal_bajo = Edna('4', '')

    def test_edad_7(self):
        # dn: NO APLICA
        # cdn: 19, 25, 30, 33, 35
        dn_normal_y_cdn_normal_1 = Edna('7', None, '31')
        self.assertEqual(dn_normal_y_cdn_normal_1.resultados[DESEMPENO_NARRATIVO]['resultado'], 'NO APLICA')
        self.assertEqual(dn_normal_y_cdn_normal_1.resultados[DESEMPENO_NARRATIVO]['percentil'], 'NO APLICA')
        self.assertEqual(dn_normal_y_cdn_normal_1.resultados[COMPRENSION_DISCURSO_NARRATIVO]['resultado'],
                         'Normal')
        self.assertEqual(dn_normal_y_cdn_normal_1.resultados[COMPRENSION_DISCURSO_NARRATIVO]['percentil'],
                         'Menor a p75')

    def test_edad_10(self):
        # dn: 15, 18, 20, 22, 23
        # cdn: 30, 34, 35, 37, 38
        dn_normal_y_cdn_normal_1 = Edna('10', '23', '38')
        dn_normal_y_cdn_normal_2 = Edna('10', '24', '39')
        self.assertEqual(dn_normal_y_cdn_normal_1.resultados[DESEMPENO_NARRATIVO]['resultado'], 'Normal')
        self.assertEqual(dn_normal_y_cdn_normal_1.resultados[DESEMPENO_NARRATIVO]['percentil'], 'Igual a p90')
        self.assertEqual(dn_normal_y_cdn_normal_1.resultados[COMPRENSION_DISCURSO_NARRATIVO]['resultado'],
                         'Normal')
        self.assertEqual(dn_normal_y_cdn_normal_1.resultados[COMPRENSION_DISCURSO_NARRATIVO]['percentil'],
                         'Igual a p90')

        self.assertEqual(dn_normal_y_cdn_normal_2.resultados[DESEMPENO_NARRATIVO]['resultado'], 'Normal')
        self.assertEqual(dn_normal_y_cdn_normal_2.resultados[DESEMPENO_NARRATIVO]['percentil'], 'Superior a p90')
        self.assertEqual(dn_normal_y_cdn_normal_2.resultados[COMPRENSION_DISCURSO_NARRATIVO]['resultado'],
                         'Normal')
        self.assertEqual(dn_normal_y_cdn_normal_2.resultados[COMPRENSION_DISCURSO_NARRATIVO]['percentil'],
                         'Superior a p90')


if __name__ == '__main__':
    print('Unit test EDNA')
    unittest.main()
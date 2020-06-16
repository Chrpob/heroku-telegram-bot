import unittest
from modelos.pecfo import Pecfo, PTJE_TOTAL, PTJE_CONCIENCIA_SILABICA, PTJE_CONCIENCIA_FONEMICA

class TestEdna(unittest.TestCase):
    def test_edad_4(self):
        print("test_edad_4")
        # PTJE TOTAL
        # 4 anos: 12, 16, 22, 26, 32
        # PTJE CONCIENCIA SILABICA
        # 4 anos: 7, 12, 15, 17, 22
        # PTJE CONCIENCIA FONEMICA
        # 4 anos: 4, 5, 8, 9, 12
        p5_p5_p5 = Pecfo('4', '5', '4', '3')
        p10_p5_p5 = Pecfo('4', '12', '4', '2')
        p5_p10_p10 = Pecfo('4', '5', '7', '4')
        self.assertEqual(p5_p5_p5.resultados[PTJE_TOTAL]['resultado'], 'Deficit')
        self.assertEqual(p5_p5_p5.resultados[PTJE_TOTAL]['percentil'], 'Menor a p10')
        self.assertEqual(p5_p5_p5.resultados[PTJE_CONCIENCIA_SILABICA]['resultado'], 'Deficit')
        self.assertEqual(p5_p5_p5.resultados[PTJE_CONCIENCIA_SILABICA]['percentil'], 'Menor a p10')
        self.assertEqual(p5_p5_p5.resultados[PTJE_CONCIENCIA_FONEMICA]['resultado'], 'Deficit')
        self.assertEqual(p5_p5_p5.resultados[PTJE_CONCIENCIA_FONEMICA]['percentil'], 'Menor a p10')

        self.assertEqual(p10_p5_p5.resultados[PTJE_TOTAL]['resultado'], 'Deficit')
        self.assertEqual(p10_p5_p5.resultados[PTJE_TOTAL]['percentil'], 'Igual a p10')
        self.assertEqual(p10_p5_p5.resultados[PTJE_CONCIENCIA_SILABICA]['resultado'], 'Deficit')
        self.assertEqual(p10_p5_p5.resultados[PTJE_CONCIENCIA_SILABICA]['percentil'], 'Menor a p10')
        self.assertEqual(p10_p5_p5.resultados[PTJE_CONCIENCIA_FONEMICA]['resultado'], 'Deficit')
        self.assertEqual(p10_p5_p5.resultados[PTJE_CONCIENCIA_FONEMICA]['percentil'], 'Menor a p10')

        self.assertEqual(p5_p10_p10.resultados[PTJE_TOTAL]['resultado'], 'Deficit')
        self.assertEqual(p5_p10_p10.resultados[PTJE_TOTAL]['percentil'], 'Menor a p10')
        self.assertEqual(p5_p10_p10.resultados[PTJE_CONCIENCIA_SILABICA]['resultado'], 'Deficit')
        self.assertEqual(p5_p10_p10.resultados[PTJE_CONCIENCIA_SILABICA]['percentil'], 'Igual a p10')
        self.assertEqual(p5_p10_p10.resultados[PTJE_CONCIENCIA_FONEMICA]['resultado'], 'Deficit')
        self.assertEqual(p5_p10_p10.resultados[PTJE_CONCIENCIA_FONEMICA]['percentil'], 'Igual a p10')

    def test_edad_5(self):
        # total
        # 5 anos: 20, 25, 29, 33, 39
        # silabica
        # 5 anos: 12, 16, 18, 22,  24
        # fonemica
        # 5 anos: 6, 8, 10, 12, 15
        p15_p15_p15 = Pecfo('5', '22', '14', '7')
        p25_25_25 = Pecfo('5', '25', '16', '8')

        self.assertEqual(p15_p15_p15.resultados[PTJE_TOTAL]['resultado'], 'Riesgo')
        self.assertEqual(p15_p15_p15.resultados[PTJE_TOTAL]['percentil'], 'Menor a p25')
        self.assertEqual(p15_p15_p15.resultados[PTJE_CONCIENCIA_SILABICA]['resultado'], 'Riesgo')
        self.assertEqual(p15_p15_p15.resultados[PTJE_CONCIENCIA_SILABICA]['percentil'], 'Menor a p25')
        self.assertEqual(p15_p15_p15.resultados[PTJE_CONCIENCIA_FONEMICA]['resultado'], 'Riesgo')
        self.assertEqual(p15_p15_p15.resultados[PTJE_CONCIENCIA_FONEMICA]['percentil'], 'Menor a p25')

        self.assertEqual(p25_25_25.resultados[PTJE_TOTAL]['resultado'], 'Riesgo')
        self.assertEqual(p25_25_25.resultados[PTJE_TOTAL]['percentil'], 'Igual a p25')
        self.assertEqual(p25_25_25.resultados[PTJE_CONCIENCIA_SILABICA]['resultado'], 'Riesgo')
        self.assertEqual(p25_25_25.resultados[PTJE_CONCIENCIA_SILABICA]['percentil'], 'Igual a p25')
        self.assertEqual(p25_25_25.resultados[PTJE_CONCIENCIA_FONEMICA]['resultado'], 'Riesgo')
        self.assertEqual(p25_25_25.resultados[PTJE_CONCIENCIA_FONEMICA]['percentil'], 'Igual a p25')

    def test_edad_6(self):
        # total
        # 6 anos: 27, 34, 39, 41, 47
        #silabica
        # 6 anos: 16, 21, 23, 26, 29
        #fonemica
        # 6 anos: 11, 13, 15, 17, 19
        p35_p35_p35 = Pecfo('6', '35', '22', '14')
        p50_p50_p50 = Pecfo('6', '39', '23', '15')

        self.assertEqual(p35_p35_p35.resultados[PTJE_TOTAL]['resultado'], 'Normal')
        self.assertEqual(p35_p35_p35.resultados[PTJE_TOTAL]['percentil'], 'Menor a p50')
        self.assertEqual(p35_p35_p35.resultados[PTJE_CONCIENCIA_SILABICA]['resultado'], 'Normal')
        self.assertEqual(p35_p35_p35.resultados[PTJE_CONCIENCIA_SILABICA]['percentil'], 'Menor a p50')
        self.assertEqual(p35_p35_p35.resultados[PTJE_CONCIENCIA_FONEMICA]['resultado'], 'Normal')
        self.assertEqual(p35_p35_p35.resultados[PTJE_CONCIENCIA_FONEMICA]['percentil'], 'Menor a p50')

        self.assertEqual(p50_p50_p50.resultados[PTJE_TOTAL]['resultado'], 'Normal')
        self.assertEqual(p50_p50_p50.resultados[PTJE_TOTAL]['percentil'], 'Igual a p50')
        self.assertEqual(p50_p50_p50.resultados[PTJE_CONCIENCIA_SILABICA]['resultado'], 'Normal')
        self.assertEqual(p50_p50_p50.resultados[PTJE_CONCIENCIA_SILABICA]['percentil'], 'Igual a p50')
        self.assertEqual(p50_p50_p50.resultados[PTJE_CONCIENCIA_FONEMICA]['resultado'], 'Normal')
        self.assertEqual(p50_p50_p50.resultados[PTJE_CONCIENCIA_FONEMICA]['percentil'], 'Igual a p50')

    def test_edad_7(self):
        # total
        # 7 anos: 35, 41, 44, 47, 49
        # silabica
        # 7 anos: 23, 24, 27, 29, 30
        # fonemica
        # 7 anos: 13, 17, 18, 19, 20
        p65_65_75 = Pecfo('7', '45', '28', '19')
        p80_80_90 = Pecfo('7', '48', '30', '22')

        self.assertEqual(p65_65_75.resultados[PTJE_TOTAL]['resultado'], 'Normal')
        self.assertEqual(p65_65_75.resultados[PTJE_TOTAL]['percentil'], 'Menor a p75')
        self.assertEqual(p65_65_75.resultados[PTJE_CONCIENCIA_SILABICA]['resultado'], 'Normal')
        self.assertEqual(p65_65_75.resultados[PTJE_CONCIENCIA_SILABICA]['percentil'], 'Menor a p75')
        self.assertEqual(p65_65_75.resultados[PTJE_CONCIENCIA_FONEMICA]['resultado'], 'Normal')
        self.assertEqual(p65_65_75.resultados[PTJE_CONCIENCIA_FONEMICA]['percentil'], 'Igual a p75')

        self.assertEqual(p80_80_90.resultados[PTJE_TOTAL]['resultado'], 'Normal')
        self.assertEqual(p80_80_90.resultados[PTJE_TOTAL]['percentil'], 'Menor a p90')
        self.assertEqual(p80_80_90.resultados[PTJE_CONCIENCIA_SILABICA]['resultado'], 'Normal')
        self.assertEqual(p80_80_90.resultados[PTJE_CONCIENCIA_SILABICA]['percentil'], 'Igual a p90')
        self.assertEqual(p80_80_90.resultados[PTJE_CONCIENCIA_FONEMICA]['resultado'], 'Normal')
        self.assertEqual(p80_80_90.resultados[PTJE_CONCIENCIA_FONEMICA]['percentil'], 'Superior a p90')

        pass


if __name__ == '__main__':
    print('Unit test PECFO')
    unittest.main()

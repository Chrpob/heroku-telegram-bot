import unittest
from modelos.stsg import Stsg, PTJE_RECEPTIVO, PTJE_EXPRESIVO

class TestStsg(unittest.TestCase):
    def test_edad_3(self):
        # Expresiva: 5 9 15 19 24
        # Receptiva: 22 25 30 33 36
        p5_10 = Stsg('3', '2', '22')
        self.assertEqual(p5_10.resultados[PTJE_EXPRESIVO]['resultado'], 'Desempeño gramatical deficitario')
        self.assertEqual(p5_10.resultados[PTJE_EXPRESIVO]['percentil'], 'Menor a p10')
        self.assertEqual(p5_10.resultados[PTJE_RECEPTIVO]['resultado'], 'Desempeño gramatical deficitario')
        self.assertEqual(p5_10.resultados[PTJE_RECEPTIVO]['percentil'], 'Igual a p10')
    def test_edad_4(self):
        # Expresiva: 10 17 20 24 30
        # Receptiva: 27 30 33 35 38
        p15_25 = Stsg('4', '12', '30')
        self.assertEqual(p15_25.resultados[PTJE_EXPRESIVO]['resultado'], 'Desempeño gramatical normal lento')
        self.assertEqual(p15_25.resultados[PTJE_EXPRESIVO]['percentil'], 'Menor a p25')
        self.assertEqual(p15_25.resultados[PTJE_RECEPTIVO]['resultado'], 'Desempeño gramatical normal lento')
        self.assertEqual(p15_25.resultados[PTJE_RECEPTIVO]['percentil'], 'Igual a p25')
        pass
    def test_edad_5(self):
        # Expresiva: 22 24 31 34 36
        # Receptiva: 32 34 38 41 43
        p35_50= Stsg('5', '31', '37')
        self.assertEqual(p35_50.resultados[PTJE_EXPRESIVO]['resultado'], 'Desempeño gramatical normal')
        self.assertEqual(p35_50.resultados[PTJE_EXPRESIVO]['percentil'], 'Igual a p50')
        self.assertEqual(p35_50.resultados[PTJE_RECEPTIVO]['resultado'], 'Desempeño gramatical normal')
        self.assertEqual(p35_50.resultados[PTJE_RECEPTIVO]['percentil'], 'Menor a p50')
        pass
    def test_edad_6(self):
        # Expresiva: 25 31 37 40 43
        # Receptiva: 35 38 41 42 46
        p65_75= Stsg('6', '38', '42')
        self.assertEqual(p65_75.resultados[PTJE_EXPRESIVO]['resultado'], 'Desempeño gramatical normal')
        self.assertEqual(p65_75.resultados[PTJE_EXPRESIVO]['percentil'], 'Menor a p75')
        self.assertEqual(p65_75.resultados[PTJE_RECEPTIVO]['resultado'], 'Desempeño gramatical normal')
        self.assertEqual(p65_75.resultados[PTJE_RECEPTIVO]['percentil'], 'Igual a p75')
    def test_edad_7(self):
        # Expresiva: 35 37 40 42 44
        # Receptiva: 35 38 42 43 45
        p85_90= Stsg('7', '43', '45')
        p95_80 = Stsg('7', '47', '44')
        self.assertEqual(p85_90.resultados[PTJE_EXPRESIVO]['resultado'], 'Desempeño gramatical normal')
        self.assertEqual(p85_90.resultados[PTJE_EXPRESIVO]['percentil'], 'Menor a p90')
        self.assertEqual(p85_90.resultados[PTJE_RECEPTIVO]['resultado'], 'Desempeño gramatical normal')
        self.assertEqual(p85_90.resultados[PTJE_RECEPTIVO]['percentil'], 'Igual a p90')

        self.assertEqual(p95_80.resultados[PTJE_EXPRESIVO]['resultado'], 'Desempeño gramatical normal')
        self.assertEqual(p95_80.resultados[PTJE_EXPRESIVO]['percentil'], 'Superior a p90')
        self.assertEqual(p95_80.resultados[PTJE_RECEPTIVO]['resultado'], 'Desempeño gramatical normal')
        self.assertEqual(p95_80.resultados[PTJE_RECEPTIVO]['percentil'], 'Menor a p90')



if __name__ == '__main__':
    unittest.main()



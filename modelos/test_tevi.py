import unittest
from modelos.tevi import Tevi, SOBRESALIENTE, MUY_BUENO, NORMAL, RETRASO_LEVE, RETRASO_GRAVE, PUNTAJE_NO_VALIDO


class TestTevi(unittest.TestCase):
    def test_edad_2(self):
        sobresaliente = Tevi(2, 28, 0)
        muy_bueno = Tevi(2, 20, 0)
        normal = Tevi(2, 12, 0)
        retraso_leve = Tevi(2, 5, 0)
        retraso_grave = Tevi(2, 1, 0)

        self.assertEqual(sobresaliente.resultado, SOBRESALIENTE)
        self.assertEqual(muy_bueno.resultado, MUY_BUENO)
        self.assertEqual(normal.resultado, NORMAL)
        self.assertEqual(retraso_leve.resultado, RETRASO_LEVE)
        self.assertEqual(retraso_grave.resultado, RETRASO_GRAVE)

    def test_edad_3(self):
        sobresaliente = Tevi(3, 35, 0)
        muy_bueno     = Tevi(3, 30, 0)
        normal        = Tevi(3, 24, 0)
        retraso_leve  = Tevi(3, 18, 0)
        retraso_grave = Tevi(3, 13, 0)

        self.assertEqual(sobresaliente.resultado, SOBRESALIENTE)
        self.assertEqual(muy_bueno.resultado, MUY_BUENO)
        self.assertEqual(normal.resultado, NORMAL)
        self.assertEqual(retraso_leve.resultado, RETRASO_LEVE)
        self.assertEqual(retraso_grave.resultado, RETRASO_GRAVE)

    def test_edad_4(self):
        sobresaliente = Tevi(4, 51, 0)
        muy_bueno     = Tevi(4, 42, 0)
        normal        = Tevi(4, 34, 0)
        retraso_leve  = Tevi(4, 26, 0)
        retraso_grave = Tevi(4, 18, 0)

        self.assertEqual(sobresaliente.resultado, SOBRESALIENTE)
        self.assertEqual(muy_bueno.resultado, MUY_BUENO)
        self.assertEqual(normal.resultado, NORMAL)
        self.assertEqual(retraso_leve.resultado, RETRASO_LEVE)
        self.assertEqual(retraso_grave.resultado, RETRASO_GRAVE)

    def test_edad_5(self):
        sobresaliente = Tevi(5, 62, 0)
        muy_bueno     = Tevi(5, 46, 0)
        normal        = Tevi(5, 46, 7)
        retraso_leve  = Tevi(5, 31, 0)
        retraso_grave = Tevi(5, 24, 0)

        self.assertEqual(sobresaliente.resultado, SOBRESALIENTE)
        self.assertEqual(muy_bueno.resultado, MUY_BUENO)
        self.assertEqual(normal.resultado, NORMAL)
        self.assertEqual(retraso_leve.resultado, RETRASO_LEVE)
        self.assertEqual(retraso_grave.resultado, RETRASO_GRAVE)

    def test_edad_6(self):
        sobresaliente = Tevi(6, 61, 0)
        muy_bueno     = Tevi(6, 54, 0)
        normal        = Tevi(6, 47, 0)
        retraso_leve  = Tevi(6, 41, 0)
        retraso_grave = Tevi(6, 34, 0)

        self.assertEqual(sobresaliente.resultado, SOBRESALIENTE)
        self.assertEqual(muy_bueno.resultado, MUY_BUENO)
        self.assertEqual(normal.resultado, NORMAL)
        self.assertEqual(retraso_leve.resultado, RETRASO_LEVE)
        self.assertEqual(retraso_grave.resultado, RETRASO_GRAVE)

    def test_edad_7(self):
        puntaje_no_valido = Tevi(7, 28, 0)
        sobresaliente = Tevi(7, 71, 0)
        muy_bueno     = Tevi(7, 64, 0)
        normal        = Tevi(7, 56, 0)
        retraso_leve  = Tevi(7, 48, 0)
        retraso_grave = Tevi(7, 40, 0)

        self.assertEqual(puntaje_no_valido.resultado, PUNTAJE_NO_VALIDO)
        self.assertEqual(sobresaliente.resultado, SOBRESALIENTE)
        self.assertEqual(muy_bueno.resultado,     MUY_BUENO)
        self.assertEqual(normal.resultado,        NORMAL)
        self.assertEqual(retraso_leve.resultado,  RETRASO_LEVE)
        self.assertEqual(retraso_grave.resultado, RETRASO_GRAVE)

    def test_edad_8(self):
        sobresaliente = Tevi(8, 71, 0)
        muy_bueno     = Tevi(8, 64, 0)
        normal        = Tevi(8, 64, 8)
        retraso_leve  = Tevi(8, 48, 0)
        retraso_grave = Tevi(8, 40, 0)

        self.assertEqual(sobresaliente.resultado, SOBRESALIENTE)
        self.assertEqual(muy_bueno.resultado,     MUY_BUENO)
        self.assertEqual(normal.resultado,        NORMAL)
        self.assertEqual(retraso_leve.resultado,  RETRASO_LEVE)
        self.assertEqual(retraso_grave.resultado, RETRASO_GRAVE)

    def test_edad_9_10(self):
        sobresaliente = Tevi(9, 84, 0)
        muy_bueno     = Tevi(10, 74, 0)
        normal        = Tevi(9, 63, 0)
        retraso_leve  = Tevi(10, 51, 0)
        retraso_grave = Tevi(9, 40, 0)

        self.assertEqual(sobresaliente.resultado, SOBRESALIENTE)
        self.assertEqual(muy_bueno.resultado,     MUY_BUENO)
        self.assertEqual(normal.resultado,        NORMAL)
        self.assertEqual(retraso_leve.resultado,  RETRASO_LEVE)
        self.assertEqual(retraso_grave.resultado, RETRASO_GRAVE)

    def test_edad_11_12(self):
        sobresaliente = Tevi(12, 104, 0)
        muy_bueno     = Tevi(11, 88, 0)
        normal        = Tevi(12, 73, 0)
        retraso_leve  = Tevi(11, 58, 0)
        retraso_grave = Tevi(12, 42, 0)

        self.assertEqual(sobresaliente.resultado, SOBRESALIENTE)
        self.assertEqual(muy_bueno.resultado,     MUY_BUENO)
        self.assertEqual(normal.resultado,        NORMAL)
        self.assertEqual(retraso_leve.resultado,  RETRASO_LEVE)
        self.assertEqual(retraso_grave.resultado, RETRASO_GRAVE)

    def test_edad_13_14(self):
        sobresaliente = Tevi(14, 111, 0)
        muy_bueno     = Tevi(13, 97, 0)
        normal        = Tevi(14, 83, 0)
        retraso_leve  = Tevi(13, 69, 0)
        retraso_grave = Tevi(14, 55, 0)

        self.assertEqual(sobresaliente.resultado, SOBRESALIENTE)
        self.assertEqual(muy_bueno.resultado,     MUY_BUENO)
        self.assertEqual(normal.resultado,        NORMAL)
        self.assertEqual(retraso_leve.resultado,  RETRASO_LEVE)
        self.assertEqual(retraso_grave.resultado, RETRASO_GRAVE)

    def test_edad_15_16_17_18(self):
        sobresaliente = Tevi(15, 116, 0)
        muy_bueno     = Tevi(16, 107, 0)
        normal        = Tevi(17, 97, 0)
        retraso_leve  = Tevi(18, 86, 0)
        retraso_grave = Tevi(15, 76, 0)

        self.assertEqual(sobresaliente.resultado, SOBRESALIENTE)
        self.assertEqual(muy_bueno.resultado,     MUY_BUENO)
        self.assertEqual(normal.resultado,        NORMAL)
        self.assertEqual(retraso_leve.resultado,  RETRASO_LEVE)
        self.assertEqual(retraso_grave.resultado, RETRASO_GRAVE)


if __name__ == '__main__':
    unittest.main

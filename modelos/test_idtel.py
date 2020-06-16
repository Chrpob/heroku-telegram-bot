import unittest
from modelos.idtel import Idtel, FONOLOGICO, MORFOLOGICO, SEMANTICO, PRAGMATICO, BAJO_LO_ESPERADO, TOTAL, ESPERADO_PARA_LA_EDAD, NO_PRESENTA_TEL, PRESENTA_TEL

class TestIdtel(unittest.TestCase):
    def test_edad_6(self):
        no_fono_morfo_no_semantico_pragmatico_no_tel = Idtel('6', '18', '15', '25', '9')
        fono_no_morfo_semantico_no_pragmatico_no_tel = Idtel('6', '15', '18', '21', '15')
        no_fono_morfo_no_semantico_pragmatico_tel    = Idtel('6', '18', '5', '25', '1')
        fono_no_morfo_semantico_no_pragmatico_tel    = Idtel('6', '5', '18', '11', '15')

        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_no_tel.resultados[FONOLOGICO], ESPERADO_PARA_LA_EDAD)
        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_no_tel.resultados[MORFOLOGICO], BAJO_LO_ESPERADO)
        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_no_tel.resultados[SEMANTICO], ESPERADO_PARA_LA_EDAD)
        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_no_tel.resultados[PRAGMATICO], BAJO_LO_ESPERADO)
        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_no_tel.resultados[TOTAL], NO_PRESENTA_TEL)

        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_no_tel.resultados[FONOLOGICO], BAJO_LO_ESPERADO)
        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_no_tel.resultados[MORFOLOGICO], ESPERADO_PARA_LA_EDAD)
        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_no_tel.resultados[SEMANTICO], BAJO_LO_ESPERADO)
        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_no_tel.resultados[PRAGMATICO], ESPERADO_PARA_LA_EDAD)
        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_no_tel.resultados[TOTAL], NO_PRESENTA_TEL)

        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_tel.resultados[FONOLOGICO], ESPERADO_PARA_LA_EDAD)
        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_tel.resultados[MORFOLOGICO], BAJO_LO_ESPERADO)
        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_tel.resultados[SEMANTICO], ESPERADO_PARA_LA_EDAD)
        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_tel.resultados[PRAGMATICO], BAJO_LO_ESPERADO)
        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_tel.resultados[TOTAL], PRESENTA_TEL)

        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_tel.resultados[FONOLOGICO], BAJO_LO_ESPERADO)
        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_tel.resultados[MORFOLOGICO], ESPERADO_PARA_LA_EDAD)
        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_tel.resultados[SEMANTICO], BAJO_LO_ESPERADO)
        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_tel.resultados[PRAGMATICO], ESPERADO_PARA_LA_EDAD)
        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_tel.resultados[TOTAL], PRESENTA_TEL)

    def test_edad_8(self):
        no_fono_morfo_no_semantico_pragmatico_no_tel = Idtel('8', '32', '27', '45', '15')
        fono_no_morfo_semantico_no_pragmatico_no_tel = Idtel('8', '27', '33', '39', '21')
        no_fono_morfo_no_semantico_pragmatico_tel    = Idtel('8', '28', '22', '41', '5')
        fono_no_morfo_semantico_no_pragmatico_tel    = Idtel('8', '20', '29', '20', '17')

        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_no_tel.resultados[FONOLOGICO], ESPERADO_PARA_LA_EDAD)
        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_no_tel.resultados[MORFOLOGICO], BAJO_LO_ESPERADO)
        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_no_tel.resultados[SEMANTICO], ESPERADO_PARA_LA_EDAD)
        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_no_tel.resultados[PRAGMATICO], BAJO_LO_ESPERADO)
        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_no_tel.resultados[TOTAL], NO_PRESENTA_TEL)

        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_no_tel.resultados[FONOLOGICO], BAJO_LO_ESPERADO)
        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_no_tel.resultados[MORFOLOGICO], ESPERADO_PARA_LA_EDAD)
        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_no_tel.resultados[SEMANTICO], BAJO_LO_ESPERADO)
        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_no_tel.resultados[PRAGMATICO], ESPERADO_PARA_LA_EDAD)
        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_no_tel.resultados[TOTAL], NO_PRESENTA_TEL)

        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_tel.resultados[FONOLOGICO], ESPERADO_PARA_LA_EDAD)
        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_tel.resultados[MORFOLOGICO], BAJO_LO_ESPERADO)
        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_tel.resultados[SEMANTICO], ESPERADO_PARA_LA_EDAD)
        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_tel.resultados[PRAGMATICO], BAJO_LO_ESPERADO)
        self.assertEqual(no_fono_morfo_no_semantico_pragmatico_tel.resultados[TOTAL], PRESENTA_TEL)

        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_tel.resultados[FONOLOGICO], BAJO_LO_ESPERADO)
        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_tel.resultados[MORFOLOGICO], ESPERADO_PARA_LA_EDAD)
        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_tel.resultados[SEMANTICO], BAJO_LO_ESPERADO)
        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_tel.resultados[PRAGMATICO], ESPERADO_PARA_LA_EDAD)
        self.assertEqual(fono_no_morfo_semantico_no_pragmatico_tel.resultados[TOTAL], PRESENTA_TEL)


if __name__ == '__main__':
    unittest.main()

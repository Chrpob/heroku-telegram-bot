# IDTEL es el que no tiene documentacion
FONOLOGICO = 'fonologico'
MORFOLOGICO = 'morfologico'
SEMANTICO = 'semantico'
PRAGMATICO = 'pragmatico'
TOTAL = 'total'

PRESENTA_TEL = 'Presenta TEL'
NO_PRESENTA_TEL = 'No presenta TEL'

BAJO_LO_ESPERADO = 'Bajo lo esperado'
ESPERADO_PARA_LA_EDAD = 'Esperado para la edad'



class Idtel(object):
    def __init__(self, _edad, _fonologico, _morfologico, _semantico, _pragmatico):
        self.edad = int(_edad)
        self.scores = {
            FONOLOGICO: int(_fonologico),
            MORFOLOGICO: int(_morfologico),
            SEMANTICO: int(_semantico),
            PRAGMATICO: int(_pragmatico),
        }
        total = 0
        for key in [FONOLOGICO, MORFOLOGICO, SEMANTICO, PRAGMATICO]:
            total += self.scores[key]
        self.scores[TOTAL] = total

        self.matriz = {}
        self.resultados = {}
        self.set_parametros()
        self.fit()

    def __repr__(self):
        texto = ''
        pruebas = [FONOLOGICO, MORFOLOGICO, SEMANTICO, PRAGMATICO, TOTAL]
        for prueba in pruebas:
            texto += f"Resultados prueba {prueba}: {self.resultados[prueba]}\n"
        return texto

    def set_parametros(self):
        if (self.edad >= 6) and (self.edad <= 7):
            self.matriz = {
                FONOLOGICO: 17,
                MORFOLOGICO: 17,
                SEMANTICO: 22,
                PRAGMATICO: 10,
                TOTAL: 66,
            }
        elif (self.edad >= 8) and (self.edad <= 9):
            self.matriz = {
                FONOLOGICO: 27,
                MORFOLOGICO: 28,
                SEMANTICO: 40,
                PRAGMATICO: 16,
                TOTAL: 111,
            }

    def fit(self):
        pruebas = [FONOLOGICO, MORFOLOGICO, SEMANTICO, PRAGMATICO, TOTAL]
        for prueba in pruebas:
            if prueba == TOTAL:
                if (self.scores[prueba] <= self.matriz[prueba]):
                    self.resultados[prueba] = PRESENTA_TEL
                else:
                    self.resultados[prueba] = NO_PRESENTA_TEL
            else:
                if (self.scores[prueba] <= self.matriz[prueba]):
                    self.resultados[prueba] = BAJO_LO_ESPERADO
                else:
                    self.resultados[prueba] = ESPERADO_PARA_LA_EDAD


if __name__ == '__main__':
    print("STUB para IDTEL")
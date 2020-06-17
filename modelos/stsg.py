from modelos.percentil import Percentil

PTJE_EXPRESIVO = 'puntaje_expresivo'
PTJE_RECEPTIVO = 'puntaje_receptivo'

LEER = {
    PTJE_EXPRESIVO: 'Resultado expresivo',
    PTJE_RECEPTIVO: 'Resultado receptivo'
}

class Stsg(Percentil):
    def __init__(self, _edad, _ptje_expresivo, _ptje_receptivo):
        super().__init__(_edad)
        self.score = {
            PTJE_EXPRESIVO: int(_ptje_expresivo),
            PTJE_RECEPTIVO: int(_ptje_receptivo),
        }
        self.get_percentiles()
        self.fit_desempeno_gramatical_normal_normal_lento_deficitario([PTJE_EXPRESIVO, PTJE_RECEPTIVO],
                                       ['p10'], ['p25'], ['p50', 'p75', 'p90'])
    def __repr__(self):
        texto = ''
        for prueba in [PTJE_EXPRESIVO, PTJE_RECEPTIVO]:
            texto += f"{LEER[prueba]}: {self.resultados[prueba]['resultado']}\nPercentil: {self.resultados[prueba]['percentil']}\n\n"
        return texto

    def get_percentiles(self):
        if self.edad == 3:
            self.matriz = {
                PTJE_EXPRESIVO: {
                    'p10': 5,
                    'p25': 9,
                    'p50': 15,
                    'p75': 19,
                    'p90': 24,
                }, PTJE_RECEPTIVO: {
                    'p10': 22,
                    'p25': 25,
                    'p50': 30,
                    'p75': 33,
                    'p90': 36,
                }
            }
        elif self.edad == 4:
            self.matriz = {
                PTJE_EXPRESIVO: {
                    'p10': 10,
                    'p25': 17,
                    'p50': 20,
                    'p75': 24,
                    'p90': 30,
                }, PTJE_RECEPTIVO: {
                    'p10': 27,
                    'p25': 30,
                    'p50': 33,
                    'p75': 35,
                    'p90': 38,
                }
            }
        elif self.edad == 5:
            self.matriz = {
                PTJE_EXPRESIVO: {
                    'p10': 22,
                    'p25': 24,
                    'p50': 31,
                    'p75': 34,
                    'p90': 36,
                }, PTJE_RECEPTIVO: {
                    'p10': 32,
                    'p25': 34,
                    'p50': 38,
                    'p75': 41,
                    'p90': 43,
                }
            }
        elif self.edad == 6:
            self.matriz = {
                PTJE_EXPRESIVO: {
                    'p10': 25,
                    'p25': 31,
                    'p50': 37,
                    'p75': 40,
                    'p90': 43,
                }, PTJE_RECEPTIVO: {
                    'p10': 35,
                    'p25': 38,
                    'p50': 41,
                    'p75': 42,
                    'p90': 46,
                }
            }
        elif self.edad == 7:
            self.matriz = {
                PTJE_EXPRESIVO: {
                    'p10': 35,
                    'p25': 37,
                    'p50': 40,
                    'p75': 42,
                    'p90': 44,
                }, PTJE_RECEPTIVO: {
                    'p10': 35,
                    'p25': 38,
                    'p50': 42,
                    'p75': 43,
                    'p90': 45,
                }
            }


from modelos.percentil import Percentil

PTJE_TOTAL = 'puntaje_total'
PTJE_CONCIENCIA_SILABICA = 'puntaje_conciencia_silabica'
PTJE_CONCIENCIA_FONEMICA = 'puntaje_conciencia_fonemica'

LEER = {
    PTJE_TOTAL: 'Puntaje total',
    PTJE_CONCIENCIA_SILABICA: 'Puntaje conciencia silábica',
    PTJE_CONCIENCIA_FONEMICA: 'Puntaje conciencia fonémica'
}

class Pecfo(Percentil):
    def __init__(self, _edad, _ptje_total, _ptje_conciencia_silabica, _ptje_conciencia_fonemica):
        super().__init__(_edad)
        self.score = {
            PTJE_TOTAL: int(_ptje_total),
            PTJE_CONCIENCIA_SILABICA: int(_ptje_conciencia_silabica),
            PTJE_CONCIENCIA_FONEMICA: int(_ptje_conciencia_fonemica),
        }
        self.get_percentiles()
        self.fit_normal_riesgo_deficit([PTJE_TOTAL, PTJE_CONCIENCIA_SILABICA, PTJE_CONCIENCIA_FONEMICA],
                                       ['p10'], ['p25'], ['p50', 'p75', 'p90'])

    def __repr__(self):
        texto = ''
        for prueba in [PTJE_TOTAL, PTJE_CONCIENCIA_SILABICA, PTJE_CONCIENCIA_FONEMICA]:
            texto += f"{LEER[prueba]}: {self.resultados[prueba]['resultado']}\nPercentil: {self.resultados[prueba]['percentil']}\n\n"
        return texto


    def get_percentiles(self):
        if self.edad == 4:
            self.matriz[PTJE_TOTAL] = {
                'p10': 12,
                'p25': 16,
                'p50': 22,
                'p75': 26,
                'p90': 32,
            }
            self.matriz[PTJE_CONCIENCIA_SILABICA] = {
                'p10': 7,
                'p25': 12,
                'p50': 15,
                'p75': 17,
                'p90': 22,
            }
            self.matriz[PTJE_CONCIENCIA_FONEMICA] = {
                'p10': 4,
                'p25': 5,
                'p50': 8,
                'p75': 9,
                'p90': 12,
            }
        elif self.edad == 5:
            self.matriz = {
                PTJE_TOTAL: {
                    'p10': 20,
                    'p25': 25,
                    'p50': 29,
                    'p75': 33,
                    'p90': 39,
                }, PTJE_CONCIENCIA_SILABICA: {
                    'p10': 12,
                    'p25': 16,
                    'p50': 18,
                    'p75': 22,
                    'p90': 24,
                }, PTJE_CONCIENCIA_FONEMICA: {
                    'p10': 6,
                    'p25': 8,
                    'p50': 10,
                    'p75': 12,
                    'p90': 15,
                }
            }
        elif self.edad == 6:
            self.matriz = {
                 PTJE_TOTAL: {
                     'p10': 27,
                     'p25': 34,
                     'p50': 39,
                     'p75': 41,
                     'p90': 47,
                 }, PTJE_CONCIENCIA_SILABICA: {
                     'p10': 16,
                     'p25': 21,
                     'p50': 23,
                     'p75': 26,
                     'p90': 29,
                 }, PTJE_CONCIENCIA_FONEMICA: {
                     'p10': 11,
                     'p25': 13,
                     'p50': 15,
                     'p75': 17,
                     'p90': 19,
                 }
            }
        elif self.edad == 7:
            self.matriz = {
                PTJE_TOTAL: {
                    'p10': 35,
                    'p25': 41,
                    'p50': 44,
                    'p75': 47,
                    'p90': 49,
                }, PTJE_CONCIENCIA_SILABICA: {
                    'p10': 23,
                    'p25': 24,
                    'p50': 27,
                    'p75': 29,
                    'p90': 30,

                }, PTJE_CONCIENCIA_FONEMICA: {
                    'p10': 13,
                    'p25': 17,
                    'p50': 18,
                    'p75': 19,
                    'p90': 20,
                }
            }

VOCABULARIO = 'vocabulario'
MORFOLOGIA = 'morfologia'
SINTAXIS = 'sintaxis'
TOTAL = 'total'

PROMEDIO = 'promedio'
SD = 'sd'

NORMAL = 'normal'
RIESGO = 'riesgo'
DEFICIT = 'deficit'

RESULTADO = 'resultado'
N_DESVIACION_ESTANDAR = 'n_desviacion_estandar'


class Tecal(object):
    def __init__(self, _edad, _vocabulario, _morfologia, _sintaxis, _total):
        self.edad = int(_edad)
        self.scores = {
            VOCABULARIO: float(_vocabulario),
            MORFOLOGIA: float(_morfologia),
            SINTAXIS: float(_sintaxis),
            TOTAL: float(_total),
        }
        self.matriz = {}
        self.resultados = {}
        self.set_parametros()
        self.fit()

    def __repr__(self):
        texto = ''
        for prueba in [VOCABULARIO, MORFOLOGIA, SINTAXIS, TOTAL]:
            texto += f"Resultado {prueba}: {self.resultados[prueba][RESULTADO]}\nFactor número de desviación estándar: {self.resultados[prueba][N_DESVIACION_ESTANDAR]}\n\n"
        return texto

    def set_parametros(self):
        if self.edad == 3:
            self.matriz = {
                VOCABULARIO: {
                    PROMEDIO: 23.6,
                    SD: 2.68
                },
                MORFOLOGIA: {
                    PROMEDIO: 23.13,
                    SD: 4.37
                },
                SINTAXIS: {
                    PROMEDIO: 5,
                    SD: 1.31
                },
                TOTAL: {
                    PROMEDIO: 52.26,
                    SD: 6.35
                }
            }
        elif self.edad == 4:
            self.matriz = {
                VOCABULARIO: {
                    PROMEDIO: 28.53,
                    SD: 4.15
                 },
                MORFOLOGIA: {
                    PROMEDIO: 28.5,
                    SD: 5.65
                },
                SINTAXIS: {
                    PROMEDIO: 5.9,
                    SD: 1.72
                },
                TOTAL: {
                    PROMEDIO: 62.93,
                    SD: 9.03
                }


            }
        elif self.edad == 5:
            self.matriz = {
                VOCABULARIO: {
                    PROMEDIO: 35.7,
                    SD: 2.62
                }, MORFOLOGIA: {
                    PROMEDIO: 38.96,
                    SD: 3.72
                }, SINTAXIS: {
                    PROMEDIO: 9.23,
                    SD: 1.22
                }, TOTAL: {
                    PROMEDIO: 84.1,
                    SD: 5.88
                }

            }
        elif self.edad == 6:
            self.matriz = {
                VOCABULARIO: {
                    PROMEDIO: 37.86,
                    SD: 1.99
                }, MORFOLOGIA: {
                    PROMEDIO: 41.26,
                    SD: 3.26
                }, SINTAXIS: {
                    PROMEDIO: 9.83,
                    SD: 1.34
                }, TOTAL: {
                    PROMEDIO: 89.1,
                    SD: 4.96
                }
            }

    def fit(self):
        for prueba in [VOCABULARIO, MORFOLOGIA, SINTAXIS, TOTAL]:
            puntuacion = abs(self.matriz[prueba][PROMEDIO] - self.scores[prueba]) / self.matriz[prueba][SD]
            if puntuacion <= 1:
                self.resultados[prueba] = {
                    RESULTADO: NORMAL,
                    N_DESVIACION_ESTANDAR: puntuacion
                }
            elif puntuacion <= 2:
                self.resultados[prueba] = {
                    RESULTADO: RIESGO,
                    N_DESVIACION_ESTANDAR: puntuacion
                }
            else:
                self.resultados[prueba] = {
                    RESULTADO: DEFICIT,
                    N_DESVIACION_ESTANDAR: puntuacion
                }


        # for prueba in [NORMAL, RIESGO, DEFICIT]:
        #     if (self.stp > self.matriz[prueba]['inf']) and (self.stp <= self.matriz[prueba]['sup']):
        #         self.resultados['resultado'] = prueba
        #         self.resultados['sd'] = (self.stp - self.matriz['promedio'] ) / self.matriz['sd']
        #         break

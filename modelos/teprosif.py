NORMAL = 'normal'
RIESGO = 'riesgo'
DEFICIT = 'deficit'

class Teprosif(object):
    def __init__(self, _edad, _stp):
        self.edad = int(_edad)
        self.stp = float(_stp)
        self.promedio = None
        self.normal_bajo = None
        self.normal_alto = None
        self.resultados = {}
        self.set_parametros()
        self.fit()

    def __repr__(self):
        texto = f"Resultado TEPROSIF-R: {self.resultados['resultado']}\nDesviación estándar: {self.resultados['sd']}"
        return texto

    def set_parametros(self):
        if self.edad == 3:
            self.matriz = {
                'promedio': 27.0,
                'sd': 15.1,
                NORMAL: {
                    'inf': 0.0,
                    'sup': 42.0
                }, RIESGO: {
                    'inf': 42.0,
                    'sup': 57.0
                }, DEFICIT: {
                    'inf': 57.0,
                    'sup': float('inf')
                }
            }
        elif self.edad == 4:
            self.matriz = {
                'promedio': 13.4,
                'sd': 10.0,
                NORMAL: {
                    'inf': 0.0,
                    'sup': 23.0
                }, RIESGO: {
                    'inf': 23.0,
                    'sup': 33.0
                }, DEFICIT: {
                    'inf': 33.0,
                    'sup': float('inf')
                }
            }
        elif self.edad == 5:
            self.matriz = {
                'promedio': 7.9,
                'sd': 6.4,
                NORMAL: {
                    'inf': 0.0,
                    'sup': 14.0
                }, RIESGO: {
                    'inf': 14.0,
                    'sup': 21.0
                }, DEFICIT: {
                    'inf': 21.0,
                    'sup': float('inf')
                }
            }
        elif self.edad == 6:
            self.matriz = {
                'promedio': 4.9,
                'sd': 5.1,
                NORMAL: {
                    'inf': 0.0,
                    'sup': 10.0
                }, RIESGO: {
                    'inf': 10.0,
                    'sup': 15.0
                }, DEFICIT: {
                    'inf': 15.0,
                    'sup': float('inf')
                }
            }


    def fit(self):
        for prueba in [NORMAL, RIESGO, DEFICIT]:
            if (self.stp > self.matriz[prueba]['inf']) and (self.stp <= self.matriz[prueba]['sup']):
                self.resultados['resultado'] = prueba
                self.resultados['sd'] = (self.stp - self.matriz['promedio'] ) / self.matriz['sd']
                break



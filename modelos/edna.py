from modelos.percentil import Percentil

DESEMPENO_NARRATIVO = 'desempeno_narrativo'
COMPRENSION_DISCURSO_NARRATIVO = 'comprension_discurso_narrativo'

PRUEBAS_EDNA = {
    DESEMPENO_NARRATIVO,
    COMPRENSION_DISCURSO_NARRATIVO
}

class Edna(Percentil):
    def __init__(self, _edad, _desempeno_narrativo, _comprension_desempeno_narrativo):
        super().__init__(_edad)
        if self.edad == 7:
            self.score = {
                DESEMPENO_NARRATIVO: None,
                COMPRENSION_DISCURSO_NARRATIVO: int(_comprension_desempeno_narrativo)
            }
        else:
            self.score = {
                DESEMPENO_NARRATIVO: int(_desempeno_narrativo),
                COMPRENSION_DISCURSO_NARRATIVO: int(_comprension_desempeno_narrativo)
            }
        self.get_percentiles()
        if self.edad == 7:
            self.resultados[DESEMPENO_NARRATIVO] = {
                'resultado': 'NO APLICA',
                'percentil': 'NO APLICA'
            }
            self.fit_normal_normal_bajo_deficit([COMPRENSION_DISCURSO_NARRATIVO], ['p10'], ['p25'], ['p50', 'p75', 'p90'])
        else:
            self.fit_normal_normal_bajo_deficit([DESEMPENO_NARRATIVO, COMPRENSION_DISCURSO_NARRATIVO], ['p10'], ['p25'], ['p50', 'p75', 'p90'])

    def __repr__(self):
        texto = ''
        if self.edad == 7:
            texto = 'DESEMPENO NARRATIVO NO APLICA PARA ESTA EDAD\n\n'
            lista = [COMPRENSION_DISCURSO_NARRATIVO]
        else:
            lista = [DESEMPENO_NARRATIVO, COMPRENSION_DISCURSO_NARRATIVO]
        for prueba in lista:
            texto += f"Resultado {prueba}: {self.resultados[prueba]['resultado']}\nFactor número de desviación estándar: {self.resultados[prueba]['percentil']}\n\n"
        return texto


    def get_percentiles(self):
        if self.edad == 4:
            self.matriz[DESEMPENO_NARRATIVO] = {
                'p10': 2,
                'p25': 4,
                'p50': 9,
                'p75': 12,
                'p90': 14
            }
            self.matriz[COMPRENSION_DISCURSO_NARRATIVO] = {
                'p10': 12,
                'p25': 19,
                'p50': 26,
                'p75': 30,
                'p90': 34
            }
        elif self.edad == 5:
            self.matriz[DESEMPENO_NARRATIVO] = {
                'p10': 2,
                'p25': 6,
                'p50': 11,
                'p75': 16,
                'p90': 18
            }
            self.matriz[COMPRENSION_DISCURSO_NARRATIVO] = {
                'p10': 12,
                'p25': 19,
                'p50': 26,
                'p75': 30,
                'p90': 34
            }
        elif self.edad == 6:
            self.matriz[DESEMPENO_NARRATIVO] = {
                'p10': 9,
                'p25': 11,
                'p50': 13,
                'p75': 17,
                'p90': 18
            }
            self.matriz[COMPRENSION_DISCURSO_NARRATIVO] = {
                'p10': 19,
                'p25': 25,
                'p50': 30,
                'p75': 33,
                'p90': 35
            }
        elif self.edad == 7:
            #XXX No admitido
            self.matriz[COMPRENSION_DISCURSO_NARRATIVO] = {
                'p10': 19,
                'p25': 25,
                'p50': 30,
                'p75': 33,
                'p90': 35
            }
        elif self.edad == 10:
            self.matriz[DESEMPENO_NARRATIVO] = {
                'p10': 15,
                'p25': 18,
                'p50': 20,
                'p75': 22,
                'p90': 23
            }
            self.matriz[COMPRENSION_DISCURSO_NARRATIVO] = {
                'p10': 30,
                'p25': 34,
                'p50': 35,
                'p75': 37,
                'p90': 38
            }

    def fit(self):
        if self.edad == 7:
            pruebas = [COMPRENSION_DISCURSO_NARRATIVO]
            self.resultados[DESEMPENO_NARRATIVO] = {
                'resultado': 'NO APLICA',
                'percentil': 'NO APLICA'
            }
        else:
            pruebas = [DESEMPENO_NARRATIVO, COMPRENSION_DISCURSO_NARRATIVO]
        for prueba in pruebas:
            self.resultados[prueba] = {
                'resultado': None,
                'percentil': None
            }
            encontrado = False
            for percentil in ['p10']:
                if self.score[prueba] < self.matriz[prueba][percentil]:
                    self.resultados[prueba]['resultado'] = 'Deficit'
                    self.resultados[prueba]['percentil'] = f"Menor a {percentil}"
                    encontrado = True
                    break
                elif self.score[prueba] == self.matriz[prueba][percentil]:
                    self.resultados[prueba]['resultado'] = 'Deficit'
                    self.resultados[prueba]['percentil'] = f"Igual a {percentil}"
                    encontrado = True
                    break
            if encontrado:
                continue
            for percentil in ['p25']:
                if self.score[prueba] < self.matriz[prueba][percentil]:
                    self.resultados[prueba]['resultado'] = 'Normal bajo'
                    self.resultados[prueba]['percentil'] = f"Menor a {percentil}"
                    encontrado = True
                    break
                elif self.score[prueba] == self.matriz[prueba][percentil]:
                    self.resultados[prueba]['resultado'] = 'Normal bajo'
                    self.resultados[prueba]['percentil'] = f"Igual a {percentil}"
                    encontrado = True
                    break
            if encontrado:
                continue
            for percentil in ['p50', 'p75', 'p90']:
                if self.score[prueba] < self.matriz[prueba][percentil]:
                    self.resultados[prueba]['resultado'] = 'Normal'
                    self.resultados[prueba]['percentil'] = f"Menor a {percentil}"
                    encontrado = True
                    break
                elif self.score[prueba] == self.matriz[prueba][percentil]:
                    self.resultados[prueba]['resultado'] = 'Normal'
                    self.resultados[prueba]['percentil'] = f"Igual a {percentil}"
                    encontrado = True
                    break
            if encontrado:
                continue
            else:
                self.resultados[prueba]['resultado'] = 'Normal'
                self.resultados[prueba]['percentil'] = f"Superior a {percentil}"


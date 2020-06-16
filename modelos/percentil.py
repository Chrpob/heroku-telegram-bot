class Percentil(object):
    def __init__(self, _edad):
        self.edad = int(_edad)
        self.score = {}
        self.matriz = {}
        self.resultados = {}

    def get_percentiles(self):
        raise NotImplementedError()

    def fit_normal_normal_bajo_deficit(self, pruebas, percentiles_deficit, percentiles_riesgo, percentiles_normal):
        for prueba in pruebas:
            self.resultados[prueba] = {
                'resultado': None,
                'percentil': None
            }
            encontrado = False
            for percentil in percentiles_deficit:
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

            for percentil in percentiles_riesgo:
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

            for percentil in percentiles_normal:
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
    def fit_normal_riesgo_deficit(self, pruebas, percentiles_deficit, percentiles_riesgo, percentiles_normal):
        for prueba in pruebas:
            self.resultados[prueba] = {
                'resultado': None,
                'percentil': None
            }
            encontrado = False
            for percentil in percentiles_deficit:
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

            for percentil in percentiles_riesgo:
                if self.score[prueba] < self.matriz[prueba][percentil]:
                    self.resultados[prueba]['resultado'] = 'Riesgo'
                    self.resultados[prueba]['percentil'] = f"Menor a {percentil}"
                    encontrado = True
                    break
                elif self.score[prueba] == self.matriz[prueba][percentil]:
                    self.resultados[prueba]['resultado'] = 'Riesgo'
                    self.resultados[prueba]['percentil'] = f"Igual a {percentil}"
                    encontrado = True
                    break
            if encontrado:
                continue

            for percentil in percentiles_normal:
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

    def fit_desempeno_gramatical_normal_normal_lento_deficitario(self, pruebas, percentiles_deficit, percentiles_riesgo, percentiles_normal):
        for prueba in pruebas:
            self.resultados[prueba] = {
                'resultado': None,
                'percentil': None
            }
            encontrado = False
            for percentil in percentiles_deficit:
                if self.score[prueba] < self.matriz[prueba][percentil]:
                    self.resultados[prueba]['resultado'] = 'Desempeño gramatical deficitario'
                    self.resultados[prueba]['percentil'] = f"Menor a {percentil}"
                    encontrado = True
                    break
                elif self.score[prueba] == self.matriz[prueba][percentil]:
                    self.resultados[prueba]['resultado'] = 'Desempeño gramatical deficitario'
                    self.resultados[prueba]['percentil'] = f"Igual a {percentil}"
                    encontrado = True
                    break
            if encontrado:
                continue

            for percentil in percentiles_riesgo:
                if self.score[prueba] < self.matriz[prueba][percentil]:
                    self.resultados[prueba]['resultado'] = 'Desempeño gramatical normal lento'
                    self.resultados[prueba]['percentil'] = f"Menor a {percentil}"
                    encontrado = True
                    break
                elif self.score[prueba] == self.matriz[prueba][percentil]:
                    self.resultados[prueba]['resultado'] = 'Desempeño gramatical normal lento'
                    self.resultados[prueba]['percentil'] = f"Igual a {percentil}"
                    encontrado = True
                    break
            if encontrado:
                continue

            for percentil in percentiles_normal:
                if self.score[prueba] < self.matriz[prueba][percentil]:
                    self.resultados[prueba]['resultado'] = 'Desempeño gramatical normal'
                    self.resultados[prueba]['percentil'] = f"Menor a {percentil}"
                    encontrado = True
                    break
                elif self.score[prueba] == self.matriz[prueba][percentil]:
                    self.resultados[prueba]['resultado'] = 'Desempeño gramatical normal'
                    self.resultados[prueba]['percentil'] = f"Igual a {percentil}"
                    encontrado = True
                    break
            if encontrado:
                continue
            else:
                self.resultados[prueba]['resultado'] = 'Desempeño gramatical normal'
                self.resultados[prueba]['percentil'] = f"Superior a {percentil}"

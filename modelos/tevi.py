# Pruebas TEVI. Esta es la que se ajusta a la tabla
SOBRESALIENTE = 'sobresaliente'
MUY_BUENO = "muy bueno"
NORMAL = "normal"
RETRASO_LEVE = "retraso leve"
RETRASO_GRAVE = "retraso grave"
PUNTAJE_NO_VALIDO = "puntaje no válido"


class Tevi(object):
    def __init__(self, _edad, _techo, _error):
        self.edad = int(_edad)
        self.techo = int(_techo)
        self.error = int(_error)
        self.resultado = None
        self.pT = None
        self.fit()

    def __repr__(self):
        texto = f"Resultado TEVI-R: {self.resultado}\nPuntaje TEVI-R: {self.pT}\n\n"
        return texto

    def fit(self):
        x = self.techo - self.error
        if (self.edad == 2):
            if (x <= 35):
                if ((x <= 1) and (x >= 1)):
                    self.pT = (x + 33)
                elif ((x >= 2) and (x <= 4)):
                    self.pT = (x + 34)
                elif ((x >= 5) and (x <= 7)):
                    self.pT = (x + 35)
                elif ((x >= 8) and (x <= 10)):
                    self.pT = (x + 36)
                elif ((x >= 11) and (x <= 12)):
                    self.pT = (x + 37)
                elif ((x >= 13) and (x <= 15)):
                    self.pT = (x + 38)
                elif ((x >= 16) and (x <= 18)):
                    self.pT = (x + 39)
                elif ((x >= 19) and (x <= 21)):
                    self.pT = (x + 40)
                elif ((x >= 22) and (x <= 24)):
                    self.pT = (x + 41)
                elif ((x >= 25) and (x <= 27)):
                    self.pT = (x + 42)
                elif ((x >= 28) and (x <= 30)):
                    self.pT = (x + 43)
                elif ((x >= 31) and (x <= 32)):
                    self.pT = (x + 44)
                elif ((x >= 33) and (x <= 35)):
                    self.pT = (x + 45)

                if (self.pT >= 65):
                    self.resultado = SOBRESALIENTE
                elif ((self.pT < 65) and (self.pT >= 55)):
                    self.resultado = MUY_BUENO
                elif ((self.pT <= 54) and (self.pT >= 45)):
                    self.resultado = NORMAL
                elif ((self.pT <= 44) and (self.pT >= 35)):
                    self.resultado = RETRASO_LEVE
                elif (self.pT < 35):
                    self.resultado = RETRASO_GRAVE
            else:
                self.resultado = PUNTAJE_NO_VALIDO
                self.pT = 0
                # Snackbar.make(view, "Ingrese puntaje admitido", Snackbar.LENGTH_SHORT)
                #        .setAction("Action", null).show();

        elif (self.edad == 3):
            if (x <= 41 and x >= 7):
                if ((x >= 7) and (x <= 8)):
                    self.pT = (x + 14)
                elif ((x >= 9) and (x <= 10)):
                    self.pT = (x + 15)
                elif ((x >= 11) and (x <= 12)):
                    self.pT = (x + 17)
                elif ((x >= 13) and (x <= 13)):
                    self.pT = (x + 18)
                elif ((x >= 14) and (x <= 14)):
                    self.pT = (x + 19)
                elif ((x >= 15) and (x <= 16)):
                    self.pT = (x + 20)
                elif ((x >= 17) and (x <= 17)):
                    self.pT = (x + 21)
                elif ((x >= 18) and (x <= 18)):
                    self.pT = (x + 22)
                elif ((x >= 19) and (x <= 20)):
                    self.pT = (x + 23)
                elif ((x >= 21) and (x <= 21)):
                    self.pT = (x + 24)
                elif ((x >= 22) and (x <= 22)):
                    self.pT = (x + 25)
                elif ((x >= 23) and (x <= 24)):
                    self.pT = (x + 26)
                elif ((x >= 25) and (x <= 25)):
                    self.pT = (x + 27)
                elif ((x >= 26) and (x <= 26)):
                    self.pT = (x + 28)
                elif ((x >= 27) and (x <= 28)):
                    self.pT = (x + 29)
                elif ((x >= 29) and (x <= 29)):
                    self.pT = (x + 30)
                elif ((x >= 30) and (x <= 30)):
                    self.pT = (x + 31)
                elif ((x >= 31) and (x <= 31)):
                    self.pT = (x + 32)
                elif ((x >= 32) and (x <= 33)):
                    self.pT = (x + 33)
                elif ((x >= 34) and (x <= 34)):
                    self.pT = (x + 34)
                elif ((x >= 35) and (x <= 35)):
                    self.pT = (x + 35)
                elif ((x >= 36) and (x <= 37)):
                    self.pT = (x + 36)
                elif ((x >= 38) and (x <= 38)):
                    self.pT = (x + 37)
                elif ((x >= 39) and (x <= 39)):
                    self.pT = (x + 38)
                elif ((x >= 40) and (x <= 41)):
                    self.pT = (x + 39)
                if (self.pT >= 65):
                    self.resultado = SOBRESALIENTE
                elif ((self.pT < 65) and (self.pT >= 55)):
                    self.resultado = MUY_BUENO
                elif ((self.pT <= 54) and (self.pT >= 45)):
                    self.resultado = NORMAL
                elif ((self.pT <= 44) and (self.pT >= 35)):
                    self.resultado = RETRASO_LEVE
                elif (self.pT < 35):
                    self.resultado = RETRASO_GRAVE
            else:
                self.resultado = PUNTAJE_NO_VALIDO
                self.pT = 0
                # Snackbar.make(view, "Ingrese puntaje admitido", Snackbar.LENGTH_SHORT)
                #         .setAction("Action", null).show();
        elif (self.edad == 4):
            if (x <= 60 and x >= 9):
                if ((x >= 9) and (x <= 12)):
                    self.pT = (x + 11)
                elif ((x >= 13) and (x <= 17)):
                    self.pT = (x + 12)
                elif ((x >= 18) and (x <= 22)):
                    self.pT = (x + 13)
                elif ((x >= 23) and (x <= 26)):
                    self.pT = (x + 14)
                elif ((x >= 27) and (x <= 31)):
                    self.pT = (x + 15)
                elif ((x >= 32) and (x <= 36)):
                    self.pT = (x + 16)
                elif ((x >= 37) and (x <= 41)):
                    self.pT = (x + 17)
                elif ((x >= 42) and (x <= 45)):
                    self.pT = (x + 18)
                elif ((x >= 46) and (x <= 50)):
                    self.pT = (x + 19)
                elif ((x >= 51) and (x <= 55)):
                    self.pT = (x + 20)
                elif ((x >= 56) and (x <= 60)):
                    self.pT = (x + 21)

                if (self.pT >= 65):
                    self.resultado = SOBRESALIENTE
                elif ((self.pT < 65) and (self.pT >= 55)):
                    self.resultado = MUY_BUENO
                elif ((self.pT <= 54) and (self.pT >= 45)):
                    self.resultado = NORMAL
                elif ((self.pT <= 44) and (self.pT >= 35)):
                    self.resultado = RETRASO_LEVE
                elif (self.pT < 35):
                    self.resultado = RETRASO_GRAVE
            else:
                self.resultado = PUNTAJE_NO_VALIDO
                self.pT = 0
                # Snackbar.make(view, "Ingrese puntaje admitido", Snackbar.LENGTH_SHORT)
                #         .setAction("Action", null).show();
        elif (self.edad == 5):
            if (x <= 62 and x >= 16):
                if ((x >= 16) and (x <= 16)):
                    self.pT = (x + 4)
                elif ((x >= 17) and (x <= 19)):
                    self.pT = (x + 5)
                elif ((x >= 20) and (x <= 23)):
                    self.pT = (x + 6)
                elif ((x >= 24) and (x <= 26)):
                    self.pT = (x + 7)
                elif ((x >= 27) and (x <= 29)):
                    self.pT = (x + 8)
                elif ((x >= 30) and (x <= 32)):
                    self.pT = (x + 9)
                elif ((x >= 33) and (x <= 35)):
                    self.pT = (x + 10)
                elif ((x >= 36) and (x <= 38)):
                    self.pT = (x + 11)
                elif ((x >= 39) and (x <= 42)):
                    self.pT = (x + 12)
                elif ((x >= 43) and (x <= 45)):
                    self.pT = (x + 13)
                elif ((x >= 46) and (x <= 48)):
                    self.pT = (x + 14)
                elif ((x >= 49) and (x <= 51)):
                    self.pT = (x + 15)
                elif ((x >= 52) and (x <= 54)):
                    self.pT = (x + 16)
                elif ((x >= 55) and (x <= 57)):
                    self.pT = (x + 17)
                elif ((x >= 58) and (x <= 61)):
                    self.pT = (x + 18)
                elif ((x >= 62) and (x <= 62)):
                    self.pT = (x + 19)
                if (self.pT >= 65):
                    self.resultado = SOBRESALIENTE
                elif ((self.pT < 65) and (self.pT >= 55)):
                    self.resultado = MUY_BUENO
                elif ((self.pT <= 54) and (self.pT >= 45)):
                    self.resultado = NORMAL
                elif ((self.pT <= 44) and (self.pT >= 35)):
                    self.resultado = RETRASO_LEVE
                elif (self.pT < 35):
                    self.resultado = RETRASO_GRAVE
            else:
                self.resultado = PUNTAJE_NO_VALIDO
                self.pT = 0
                # Snackbar.make(view, "Ingrese puntaje admitido", Snackbar.LENGTH_SHORT)
                #         .setAction("Action", null).show();
        elif (self.edad == 6):
            if (x <= 68 and x >= 27):
                if ((x >= 27) and (x <= 28)):
                    self.pT = (x - 7)
                elif ((x >= 29) and (x <= 31)):
                    self.pT = (x - 6)
                elif ((x >= 32) and (x <= 32)):
                    self.pT = (x - 5)
                elif ((x >= 33) and (x <= 34)):
                    self.pT = (x - 4)
                elif ((x >= 35) and (x <= 36)):
                    self.pT = (x - 3)
                elif ((x >= 37) and (x <= 38)):
                    self.pT = (x - 2)
                elif ((x >= 39) and (x <= 40)):
                    self.pT = (x - 1)
                elif ((x >= 41) and (x <= 42)):
                    self.pT = x
                elif ((x >= 43) and (x <= 44)):
                    self.pT = (x + 1)
                elif ((x >= 45) and (x <= 46)):
                    self.pT = (x + 2)
                elif ((x >= 47) and (x <= 48)):
                    self.pT = (x + 3)
                elif ((x >= 49) and (x <= 50)):
                    self.pT = (x + 4)
                elif ((x >= 51) and (x <= 53)):
                    self.pT = (x + 5)
                elif ((x >= 54) and (x <= 55)):
                    self.pT = (x + 6)
                elif ((x >= 56) and (x <= 57)):
                    self.pT = (x + 7)
                elif ((x >= 58) and (x <= 59)):
                    self.pT = (x + 8)
                elif ((x >= 60) and (x <= 61)):
                    self.pT = (x + 9)
                elif ((x >= 62) and (x <= 63)):
                    self.pT = (x + 10)
                elif ((x >= 64) and (x <= 65)):
                    self.pT = (x + 11)
                elif ((x >= 66) and (x <= 67)):
                    self.pT = (x + 12)
                elif ((x >= 68) and (x <= 68)):
                    self.pT = (x + 13)
                if (self.pT >= 65):
                    self.resultado = SOBRESALIENTE
                elif ((self.pT < 65) and (self.pT >= 55)):
                    self.resultado = MUY_BUENO
                elif ((self.pT <= 54) and (self.pT >= 45)):
                    self.resultado = NORMAL
                elif ((self.pT <= 44) and (self.pT >= 35)):
                    self.resultado = RETRASO_LEVE
                elif (self.pT < 35):
                    self.resultado = RETRASO_GRAVE
            else:
                self.resultado = PUNTAJE_NO_VALIDO
                self.pT = 0
                # Snackbar.make(view, "Ingrese puntaje admitido", Snackbar.LENGTH_SHORT)
                #         .setAction("Action", null).show();
        elif (self.edad == 7) or (self.edad == 8):
            if (x <= 79 and x >= 32):
                if ((x >= 32) and (x <= 32)):
                    self.pT = (x - 12)
                elif ((x >= 33) and (x <= 36)):
                    self.pT = (x - 11)
                elif ((x >= 37) and (x <= 40)):
                    self.pT = (x - 10)
                elif ((x >= 41) and (x <= 44)):
                    self.pT = (x - 9)
                elif ((x >= 45) and (x <= 47)):
                    self.pT = (x - 8)
                elif ((x >= 48) and (x <= 52)):
                    self.pT = (x - 7)
                elif ((x >= 53) and (x <= 55)):
                    self.pT = (x - 6)
                elif ((x >= 56) and (x <= 59)):
                    self.pT = (x - 5)
                elif ((x >= 60) and (x <= 63)):
                    self.pT = (x - 4)
                elif ((x >= 64) and (x <= 67)):
                    self.pT = (x - 3)
                elif ((x >= 68) and (x <= 70)):
                    self.pT = (x - 2)
                elif ((x >= 71) and (x <= 74)):
                    self.pT = (x - 1)
                elif ((x >= 75) and (x <= 78)):
                    self.pT = x
                elif ((x >= 79) and (x <= 79)):
                    self.pT = (x + 1)
                if (self.pT >= 65):
                    self.resultado = SOBRESALIENTE
                elif ((self.pT < 65) and (self.pT >= 55)):
                    self.resultado = MUY_BUENO
                elif ((self.pT <= 54) and (self.pT >= 45)):
                    self.resultado = NORMAL
                elif ((self.pT <= 44) and (self.pT >= 35)):
                    self.resultado = RETRASO_LEVE
                elif (self.pT < 35):
                    self.resultado = RETRASO_GRAVE
            else:
                self.resultado = PUNTAJE_NO_VALIDO
                self.pT = 0
                # Snackbar.make(view, "Ingrese puntaje admitido", Snackbar.LENGTH_SHORT)
                #         .setAction("Action", null).show();
        elif (self.edad == 9) or (self.edad == 10):
            if (x <= 97 and x >= 28):
                if ((x >= 28) and (x <= 32)):
                    self.pT = (x - 8)
                elif ((x >= 33) and (x <= 39)):
                    self.pT = (x - 9)
                elif ((x >= 40) and (x <= 46)):
                    self.pT = (x - 10)
                elif ((x >= 47) and (x <= 54)):
                    self.pT = (x - 11)
                elif ((x >= 55) and (x <= 61)):
                    self.pT = (x - 12)
                elif ((x >= 62) and (x <= 69)):
                    self.pT = (x - 13)
                elif ((x >= 70) and (x <= 76)):
                    self.pT = (x - 14)
                elif ((x >= 77) and (x <= 84)):
                    self.pT = (x - 15)
                elif ((x >= 85) and (x <= 91)):
                    self.pT = (x - 16)
                elif ((x >= 92) and (x <= 97)):
                    self.pT = (x - 17)
                if (self.pT >= 65):
                    self.resultado = SOBRESALIENTE
                elif ((self.pT < 65) and (self.pT >= 55)):
                    self.resultado = MUY_BUENO
                elif ((self.pT <= 54) and (self.pT >= 45)):
                    self.resultado = NORMAL
                elif ((self.pT <= 44) and (self.pT >= 35)):
                    self.resultado = RETRASO_LEVE
                elif (self.pT < 35):
                    self.resultado = RETRASO_GRAVE
            else:
                self.resultado = PUNTAJE_NO_VALIDO
                self.pT = 0
                # Snackbar.make(view, "Ingrese puntaje admitido", Snackbar.LENGTH_SHORT)
                #         .setAction("Action", null).show();
        elif (self.edad == 11) or (self.edad == 12):
            if (x <= 116 and x >= 27):
                if ((x >= 27) and (x <= 29)):
                    self.pT = (x - 7)
                elif ((x >= 30) and (x <= 31)):
                    self.pT = (x - 8)
                elif ((x >= 32) and (x <= 34)):
                    self.pT = (x - 9)
                elif ((x >= 35) and (x <= 37)):
                    self.pT = (x - 10)
                elif ((x >= 38) and (x <= 40)):
                    self.pT = (x - 11)
                elif ((x >= 41) and (x <= 43)):
                    self.pT = (x - 12)
                elif ((x >= 44) and (x <= 45)):
                    self.pT = (x - 13)
                elif ((x >= 46) and (x <= 48)):
                    self.pT = (x - 14)
                elif ((x >= 49) and (x <= 51)):
                    self.pT = (x - 15)
                elif ((x >= 52) and (x <= 54)):
                    self.pT = (x - 16)
                elif ((x >= 55) and (x <= 57)):
                    self.pT = (x - 17)
                elif ((x >= 58) and (x <= 59)):
                    self.pT = (x - 18)
                elif ((x >= 60) and (x <= 62)):
                    self.pT = (x - 19)
                elif ((x >= 63) and (x <= 65)):
                    self.pT = (x - 20)
                elif ((x >= 66) and (x <= 68)):
                    self.pT = (x - 21)
                elif ((x >= 69) and (x <= 71)):
                    self.pT = (x - 22)
                elif ((x >= 72) and (x <= 74)):
                    self.pT = (x - 23)
                elif ((x >= 75) and (x <= 76)):
                    self.pT = (x - 24)
                elif ((x >= 77) and (x <= 79)):
                    self.pT = (x - 25)
                elif ((x >= 80) and (x <= 82)):
                    self.pT = (x - 26)
                elif ((x >= 83) and (x <= 85)):
                    self.pT = (x - 27)
                elif ((x >= 86) and (x <= 88)):
                    self.pT = (x - 28)
                elif ((x >= 89) and (x <= 90)):
                    self.pT = (x - 29)
                elif ((x >= 91) and (x <= 93)):
                    self.pT = (x - 30)
                elif ((x >= 94) and (x <= 96)):
                    self.pT = (x - 31)
                elif ((x >= 91) and (x <= 99)):
                    self.pT = (x - 32)
                elif ((x >= 100) and (x <= 102)):
                    self.pT = (x - 33)
                elif ((x >= 103) and (x <= 104)):
                    self.pT = (x - 34)
                elif ((x >= 105) and (x <= 107)):
                    self.pT = (x - 35)
                elif ((x >= 108) and (x <= 110)):
                    self.pT = (x - 36)
                elif ((x >= 111) and (x <= 113)):
                    self.pT = (x - 37)
                elif ((x >= 114) and (x <= 116)):
                    self.pT = (x - 38)
                if (self.pT >= 65):
                    self.resultado = SOBRESALIENTE
                elif ((self.pT < 65) and (self.pT >= 55)):
                    self.resultado = MUY_BUENO
                elif ((self.pT <= 54) and (self.pT >= 45)):
                    self.resultado = NORMAL
                elif ((self.pT <= 44) and (self.pT >= 35)):
                    self.resultado = RETRASO_LEVE
                elif (self.pT < 35):
                    self.resultado = RETRASO_GRAVE
            else:
                self.resultado = PUNTAJE_NO_VALIDO
                self.pT = 0
                # Snackbar.make(view, "Ingrese puntaje admitido", Snackbar.LENGTH_SHORT)
                #         .setAction("Action", null).show();
        elif (self.edad == 13) or (self.edad == 14):
            if (x <= 116 and x >= 41):
                if ((x >= 41) and (x <= 43)):
                    self.pT = (x - 21)
                elif ((x >= 44) and (x <= 46)):
                    self.pT = (x - 22)
                elif ((x >= 47) and (x <= 50)):
                    self.pT = (x - 23)
                elif ((x >= 51) and (x <= 53)):
                    self.pT = (x - 24)
                elif ((x >= 54) and (x <= 57)):
                    self.pT = (x - 25)
                elif ((x >= 58) and (x <= 60)):
                    self.pT = (x - 26)
                elif ((x >= 61) and (x <= 64)):
                    self.pT = (x - 27)
                elif ((x >= 65) and (x <= 67)):
                    self.pT = (x - 28)
                elif ((x >= 68) and (x <= 71)):
                    self.pT = (x - 29)
                elif ((x >= 72) and (x <= 74)):
                    self.pT = (x - 30)
                elif ((x >= 75) and (x <= 78)):
                    self.pT = (x - 31)
                elif ((x >= 79) and (x <= 81)):
                    self.pT = (x - 32)
                elif ((x >= 82) and (x <= 84)):
                    self.pT = (x - 33)
                elif ((x >= 85) and (x <= 88)):
                    self.pT = (x - 34)
                elif ((x >= 89) and (x <= 91)):
                    self.pT = (x - 35)
                elif ((x >= 92) and (x <= 95)):
                    self.pT = (x - 36)
                elif ((x >= 96) and (x <= 98)):
                    self.pT = (x - 37)
                elif ((x >= 99) and (x <= 102)):
                    self.pT = (x - 38)
                elif ((x >= 103) and (x <= 105)):
                    self.pT = (x - 39)
                elif ((x >= 106) and (x <= 109)):
                    self.pT = (x - 40)
                elif ((x >= 110) and (x <= 112)):
                    self.pT = (x - 41)
                elif ((x >= 113) and (x <= 116)):
                    self.pT = (x - 42)
                if (self.pT >= 65):
                    self.resultado = SOBRESALIENTE
                elif ((self.pT < 65) and (self.pT >= 55)):
                    self.resultado = MUY_BUENO
                elif ((self.pT <= 54) and (self.pT >= 45)):
                    self.resultado = NORMAL
                elif ((self.pT <= 44) and (self.pT >= 35)):
                    self.resultado = RETRASO_LEVE
                elif (self.pT < 35):
                    self.resultado = RETRASO_GRAVE
            else:
                self.resultado = PUNTAJE_NO_VALIDO
                self.pT = 0
                # Snackbar.make(view, "Ingrese puntaje admitido", Snackbar.LENGTH_SHORT)
                #         .setAction("Action", null).show();
        elif (self.edad == 15) or (self.edad == 16) or (self.edad == 17) or (self.edad == 18):
            if (x <= 116 and x >= 65):
                if ((x >= 65) and (x <= 68)):
                    self.pT = (x - 45)
                elif ((x >= 69) and (x <= 95)):
                    self.pT = (x - 46)
                elif ((x >= 96) and (x <= 116)):
                    self.pT = (x - 47)
                if (self.pT >= 65):
                    self.resultado = SOBRESALIENTE
                elif ((self.pT < 65) and (self.pT >= 55)):
                    self.resultado = MUY_BUENO
                elif ((self.pT <= 54) and (self.pT >= 45)):
                    self.resultado = NORMAL
                elif ((self.pT <= 44) and (self.pT >= 35)):
                    self.resultado = RETRASO_LEVE
                elif (self.pT < 35):
                    self.resultado = RETRASO_GRAVE
            else:
                self.resultado = PUNTAJE_NO_VALIDO
                self.pT = 0
                # Snackbar.make(view, "Ingrese puntaje admitido", Snackbar.LENGTH_SHORT)
                #         .setAction("Action", null).show();

if __name__ == '__main__':
    print("Stub tevi")
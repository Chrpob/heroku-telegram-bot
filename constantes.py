TEXTO_PRINCIPAL = 'FonoaudiologaBot 🤖 es una robot que colabora optimizando el tiempo en el cálculo de desviaciones ' \
                  'estándar, percentiles y puntajes en distintas pruebas.' \
                  ' Conoce como apoyar el desarrollo del proyecto en /apoyar\n\n' \
                  'Las pruebas incluidas y comandos son:\n\n' \
                  '/edna para calcular EDNA\n' \
                  '/idtel para calcular IDTEL\n' \
                  '/pecfo para calcular PECFO\n' \
                  '/stsg para calcular STSG\n' \
                  '/teprosif para calcular TEPROSIF-R\n' \
                  '/tevi para calcular TEVI\n' \
                  '/tecal para calcular TECAL\n\n' \
                  #'Definiciones\n\n' \
                  #'/define abuso vocal\n' \
                  #'/define afasia\n' \
                  #'/define_abuso_vocal \n' \
                  #'/define_afasia'

TEXTO_APOYO = 'Puedes apoyar el proyecto comprando un café ☕ acá: https://www.buymeacoffee.com/presionaenter\n\n' \
              'Si encontraste un bug, por favor reportarlo en @PresionaEnter o en https://presionaenter.com/bug'

DEF_ABUSO_VOCAL = '- Abuso vocal\n' \
                  'Un mal uso vocal puede llevar a un abuso. Las conductas abusivas pueden ser: uso prolongado del ' \
                  'volumen, esfuerzo y uso excesivo durante un período inflamatorio, tos excesiva y carraspeo.\n' \
                  '(María Cristina A. J.-M, 2002)'
DEF_AFASIA = '- Afasia\n' \
             'Es un trastorno del lenguaje como consecuencia de una lesión en las áreas cerebrales que controlan su ' \
             'emisión y comprensión, así como sus componentes (conocimiento semántico, fonológico, morfológico, ' \
             'sintáctico).\n' \
             '(Nancy Helm-Estabrooks, 2005).'

REGEX_ONLY_STRINGS = "[a-zA-Z]+"
# REGEX_ONLY_NUMBERS = '/(\d+(\.\d+)?)/'
REGEX_ONLY_NUMBERS = '^[0-9]+$'

INCORRECTA_CANTIDAD_DE_ARGUMENTOS = 'Cantidad incorrecta de palabras para comando /define.\n'\
                                    'Intente usando una de estas dos: \n/define afasia\n/define abuso vocal'

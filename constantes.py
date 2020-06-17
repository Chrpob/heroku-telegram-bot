TEXTO_PRINCIPAL = 'Fonoaudióloga Bot es una robot que te permite obtener los calculos de las principales pruebas. \n'
                  'Además, obtener definiciones de conceptos importantes para la fonoaudiología. \n'\
                  'Puedes apoyar el desarrollo comprando un café: https://www.buymeacoffee.com/presionaenter \n' \
                  'Si encontraste algun error, por favor, informalo en https://presionaenter.com/bug \n' \ 
    
                  'Las pruebas incluidas y sus comandos son\n\n' \
              
                  '/edna para calcular el EDNA\n' \
                  '/idtel para calcular el IDTEL\n' \
                  '/pecfo para calcular el PECFO\n' \
                  '/stsg para calcular el STSG\n' \
                  '/teprosif para calcular el TEPROSIF-R\n' \
                  '/tevi para calcular el TEVI\n' \
                  '/tecal para calcular el TECAL\n\n' \
                 ## 'Definiciones\n\n' \
                  #'/define abuso vocal\n' \
                  #'/define afasia\n' \
                  #'/define_abuso_vocal \n' \
                  #'/define_afasia'

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

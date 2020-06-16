# Fonocalculadora Bot.

## Recomendación opcional

Para escribir este proyecto, se utilizó el IDE pycharm de la gente de JetBrains. Es muy fácil con pycharm
crear un ambiente virtual en python, manejar las versiones, y correr los tests. Si no sabe
como correr los tests manualmente, puede descargar el IDE pycharm y con ese podrá configurar
este proyecto rápidamente.

## Configuración local

Fonocalculadora Bot es un bot de Telegram que utiliza el wrapper python-telegram-bot para comunicarse
con la API de Telegram utilizando lenguaje python 3.6

La única dependencia que tiene este proyecto es python-telegram-bot. Puede utilizar pip para
leer el archivo requirements.txt e instalar las dependencias ya sea en los archivos de sistema,
o en su entorno virtual favorito. En requirements.txt están las dependencias de python-telegram-bot
que son 8.

Es importante que para echar a andar el bot, usted disponga de un token de telegram para bots.
¿Cómo obtener su token? Hablando con el Bot Father. Aquí puede encontrar los detalles en la
[guía oficial](https://core.telegram.org/bots#3-how-do-i-create-a-bot)

Una vez haya obtenido su token, debe incorporarlo como variable de entorno. Este bot ha sido probado
en sistema GNU/Linux.
- Hay un archivo llamado secrets.sh.sample. Copie ese archivo y péguelo
con el nombre "secrets.sh". 
- Abra el archivo, y encontrará una línea que dice lo siguiente:
> export BOT_KEY='INSERTE AQUI LA LLAVE DEL BOT'

Cambie la frase que dice INSERTE AQUI LA LLAVE DEL BOT reemplazándola por el token que
le entregó el Bot Father en el momento en que usted creó el bot. No borre las comillas simples.
La línea debería quedar como algo así:

> export BOT_KEY='hfhenvdjhfd:12374nfdsf....'

Esas letras y números ininteligibles debieran corresponderse con las letras y números ininteligibles
que conforman su propio token. Guarde el archivo y ciérrelo.

- Ahora abra un terminal, diríjase a la carpeta donde está el proyecto, y ejecute el siguiente comando:

> source sample.sh

Con este comando, usted estará cargando la variable de entorno BOT_KEY que tiene el valor de su token
en su sesión de shell de la línea de comandos. Ahora está usted listo para poder ejecutar el programa
main.py utilizando su intérprete de Python, en la misma sesión de shell donde ahora ha cargado la
nueva variable de entorno BOT_KEY.

Es importante recordar que una vez que usted cierre esa terminal, la variable de entorno
BOT_KEY se eliminará y tendrá que hacer este procedimiento de nuevo. Esto también sucederá
si apaga su computador.

¿Por qué cargamos esta variable de entorno? Porque en el programa main.py que es el que
ejecuta el bot completo, antes de cargar el bot, el programa lee con la instrucción:

> BOT_KEY = os.environ['BOT_KEY']

De la sesión de shell donde se cargó la variable de entorno BOT_KEY, y con eso su 
token de telegram queda cargado en la memoria ram del programa en python.

Esto es importante de realizar porque si usted copia y pega su token de telegram para su bot,
cualquiera que tenga acceso al código de su bot tendrá control de su bot. Podrá crear un bot
que haga cosas malas (como cometer un fraude) con un token que le pertenece a un tercero,
y luego podrían echarle la culpa a usted.

Si quiere, puede copiar y pegar su token directo en el código fuente y no tendría que
volver a hacer este ritual. Pero eso queda bajo su propia responsabilidad.

## Explicación del Programa

El programa se compone de un archivo principal que es main.py. Este programa recoge
varios ConversationHandler (que forman parte de la librería python-telegram-bot) que se 
generan en los archivos que llevan los mismos nombres de los indicadores (EDNA, IDTEL, etc).
Cada uno de estos ConversationHandlers manejan en su propio archivo la secuencia de pasos
que debe asistir el bot al usuario para obtener los datos que necesita para calcular
el resultado del indicador. Por ejemplo, el indicador EDNA necesita 3 parámetros:

- Edad
- Desempeño Narrativo
- Comprensión Desempeño Narrativo

Entonces el archivo edna.py contiene un ConversationHandler que tiene 3 estados: uno para
obtener la edad, otro para obtener el desempeño narrativo, y otro para la comprensión del 
desempeño narrativo. Este ConversationHandler maneja una conversación de 3 estados donde
en cada estado se pregunta por uno de estos parámetros.

Esta idea se replica para el resto de los indicadores, y main.py es el encargado de orquestar
a los 7 indicadores. Además de agregar unos CommandHandler para entregar las definiciones de
Abuso Vocal y Afasia.

A su vez, cada ConversationHandler importará un **modelo** que se encuentra en la subcarpeta
*modelos*. El ConversationHandler de EDNA que se encuentra en el archivo edna.py, importará
el modelo que se encuentra en modelos/edna.py

Es en la carpeta de modelos donde cada archivo que lleva el nombre de su indicador,
tiene un modelo para descubrir en qué percentil se encuentra el individuo que se
está evaluando, o para saber los resultados que tendrá un individuo que haya tomado
el indicador EDNA y haya puntuado X e Y en las dos pruebas que se le realizaron.

Toda la información de cada indicador está en esos archivos. Y además cada archivo de modelo
tiene a su correspondiente archivo de testeo, que también se encuentra en la carpeta modelos
y lleva el mismo nombre del indicador, solo que con el prefijo 'test_' agregado a su nombre.

Por lo que si queremos ver los tests del indicador EDNA, debemos ver el archivo modelos/test_edna.py
Los tests están escritos en la librería estándar de Python unittest. Los archivos de test
crean instancias del modelo de indicador que lleva su nobre, y le mandan varios parámetros determinados.
Luego de crear estas instancias, el programa contiene líneas de aserciones (assert, en inglés)
que comprueban que los resultados obtenidos por el modelo son los resultados que uno esperaba.
Si estas condiciones se cumplen: lo obtenido es lo mismo que lo esperado, entonces el
programa de test finaliza correctamente. Si no, le avisa al usuario que ocurrió un error.

Con los casos de prueba que hay en los archivos de tests, hemos podido comprobar que
para casos de pruebas conocidas, el programa devuelve lo que uno espera que debería
devolver.






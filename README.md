# Proyectos

Este repositorio contiene varios proyectos desarrollados en Python. Cada carpeta incluye un `README.md` con instrucciones y detalles del proyecto.

## Calculadora Futurista

Este proyecto es una calculadora interactiva creada con Tkinter, una biblioteca de Python para crear interfaces gráficas de usuario. La calculadora puede realizar las operaciones matemáticas básicas (suma, resta, multiplicación y división) e incluso incorpora una funcionalidad para reproducir un GIF en bucle como fondo.

El código de este proyecto se encuentra en `calculadora.py`.

**Uso:**

1. Ejecuta `python calculadora.py`.
2. Introduce la operación matemática en el campo de entrada y presiona el botón "=" para obtener el resultado.

**Dependencias:**

- tkinter
- PIL
- re
- cv2

## Ahorcado

Este proyecto es un juego de ahorcado en consola. El jugador puede adivinar una letra a la vez o intentar adivinar toda la palabra. El juego termina cuando el jugador adivina la palabra o cuando se agotan los intentos.

El código de este proyecto se encuentra en `ahorcado.py`.

**Uso:**

1. Ejecuta `python ahorcado.py`.
2. Sigue las instrucciones en consola para adivinar la palabra.

## Xtract

Este proyecto es una herramienta para extraer el audio de los archivos de video en una carpeta específica. Utiliza la biblioteca moviepy para realizar la extracción del audio.

El código de este proyecto se encuentra en `xtract.py`.

**Uso:**

1. Ejecuta `python xtract.py`.
2. Proporciona la ruta de la carpeta que contiene los videos y la ruta de la carpeta donde se guardará el audio extraído.

**Dependencias:**

- os
- moviepy

## Instalación de las Dependencias

Puedes instalar las dependencias ejecutando el siguiente comando en tu terminal:

## Visualizador de Algoritmos de Ordenamiento

Este proyecto es una visualización interactiva de varios algoritmos de ordenamiento. Permite a los usuarios seleccionar un algoritmo de ordenamiento y luego visualizar cómo el algoritmo ordena una lista de números en tiempo real.

**Código principal:**

El código está escrito en Python y hace uso de varias bibliotecas como matplotlib y tkinter para la interfaz de usuario y la visualización. Los algoritmos de ordenamiento incluyen: Selection Sort, QuickSort, y Merge Sort.

**Instrucciones de uso:**

1. Ejecute el script en Python.
2. Seleccione el algoritmo de ordenamiento que desea visualizar utilizando los botones de opción.
3. Presione el botón "Visualizar" para comenzar la visualización.

## Generador y Guardador de Contraseñas

Este proyecto es un generador de contraseñas que permite a los usuarios generar contraseñas seguras y guardarlas junto con un nombre de usuario o descriptor.

**Código principal:**

El código está escrito en Python y utiliza la biblioteca tkinter para la interfaz de usuario. La aplicación genera contraseñas que incluyen letras, números y símbolos de puntuación, y guarda las contraseñas generadas en un archivo CSV junto con un nombre de usuario y la fecha y hora en que se creó la contraseña.

**Instrucciones de uso:**

1. Ejecute el script en Python.
2. Para generar una nueva contraseña, haga clic en el botón "Generar Contraseña".
3. Para guardar una contraseña, introduzca un nombre en el campo de entrada y haga clic en "Guardar Contraseña".
4. Para ver las contraseñas guardadas, haga clic en "Contraseñas Guardadas".

# Conversor de Texto a Emoji

Este proyecto es una sencilla aplicación de Python que convierte el texto ingresado a emojis correspondientes. Este conversor de texto a emoji está actualmente en versión de prueba y solo acepta texto en inglés.

**Uso**

Para utilizar el conversor de texto a emoji, simplemente ejecuta el script `text_to_emoji.py`. Se abrirá una interfaz gráfica de usuario donde podrás introducir tu texto en el campo de entrada. Después de introducir tu texto, haz clic en el botón "Submit" para convertir el texto a emojis. El texto convertido se mostrará en el campo de resultados.

**Nota**

Este proyecto utiliza un archivo `emoji.json` que contiene un diccionario de emojis. Cada emoji en el diccionario tiene un nombre y un carácter correspondiente. El script de Python busca en este diccionario para encontrar el mejor emoji correspondiente para cada palabra del texto ingresado.

**Contribución**

Las contribuciones son bienvenidas. Por favor, sientete libre de sugerir mejoras o añadir nuevas características.

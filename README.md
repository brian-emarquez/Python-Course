
<h2 align="center">Python Course - Learn Python &nbsp;:heart:&nbsp;</h2>

![python](./Images/python3.png)

## ¿Que es Python? 💻

Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Se trata de un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional. Es un lenguaje interpretado, dinámico y multiplataforma.

Es administrado por la Python Software Foundation. Posee una licencia de código abierto, denominada Python Software Foundation License, que es compatible con la Licencia pública general de GNU a partir de la versión 2.1.1, e incompatible en ciertas versiones anteriores.
- `C:\Python27\python.exe`: Ejecutar Aplicaciones en Windows.
- `usr/bin/python`: Ejecutar Aplicaciones en Linux

### Ejemplos
```
>>> 2 + 3
5
```

```
print("Hello, World!")
```
## Comandos 🧑‍💻

_Verifica la versión de Python_

```
python --version
```

_Actualiza el  PIP de Python_

```
python -m pip install --upgrade pip
```

_Creacion de un Instalador_

```
pip install pyinstaller
```

_Creacion de un .exe_

```
pyinstaller --windowed nombreArchivo.py
```

_Creacion de un .exe - un solo archivo_

```
pyinstaller --windowed --onefile nombreArchivo.py
```

_Listado de Modulos instalados en Python_

```
pip list 
```

_Desinstalar Modulos_

```
pip uninstall nombreModulo
```

_Conector Base de datos - SQL SERVER_

```
pip install pyodbc
```

_Conector Base de datos - MariaDB_

```
pip3 install mariadb
```

_Conector Base de datos - Mysql_

```
pip install mysql-connector
```
```
pip install mysql-connector-python
```
```
pip install mysql-connector-python-rf
```

_Instalar Pillow_

```
pip install pillow
```

_Instalar Requests_

```
pip install requests
```

_Instalar Numpy_

```
pip install numpy
```

_Instalar Matplotlib_

```
pip install matplotlib
```

## Historia 📖
Python fue creado a finales de los ochenta por Guido van Rossum en el Centro para las Matemáticas y la Informática (CWI, Centrum Wiskunde & Informatica), en los Países Bajos, como un sucesor del lenguaje de programación ABC, capaz de manejar excepciones e interactuar con el sistema operativo Amoeba.

El nombre del lenguaje proviene de la afición de su creador por los humoristas británicos Monty Python.

Van Rossum es el principal autor de Python, y su continuo rol central en decidir la dirección de Python es reconocido, refiriéndose a él como Benevolente Dictador Vitalicio (en inglés: Benevolent Dictator for Life, BDFL); sin embargo el 12 de julio de 2018 declinó de dicha situación de honor sin dejar un sucesor o sucesora y con una declaración altisonante:

En 1991, van Rossum publicó el código de la versión 0.9.0 en alt.sources. En esta etapa del desarrollo ya estaban presentes clases con herencia, manejo de excepciones, funciones y los tipos modulares, como: str, list, dict, entre otros. Además en este lanzamiento inicial aparecía un sistema de módulos adoptado de Modula-3; van Rossum describe el módulo como «una de las mayores unidades de programación de Python». El modelo de excepciones en Python es parecido al de Modula-3, con la adición de una cláusula else. En el año 1994 se formó comp.lang.python, el foro de discusión principal de Python, marcando un hito en el crecimiento del grupo de usuarios de este lenguaje.
[WIKIPEDIA](https://es.wikipedia.org/wiki/Python).<br>

📦 [Install Python](https://www.python.org/) Instalador de Python.<br>
📦 [Install Anaconda](https://www.anaconda.com/) Intalador de Anaconda.<br>
📦 [Install Visual studio Code](https://code.visualstudio.com/) Intalador de Visual Studio Code
[BLOG](https://www.anaconda.com/blog).<br>


| Caracteristicas            | Visual Code |   Anaconda   |   
|----------------------------|:-----------:|:------------:|
| Codigo Abierto             |      ❌     |      ✔️     |      
| Multiplataforma            |      ✔️     |      ✔️     |     
| Soporte                    |      ✔️     |      ✔️     |      
| Ciencia de datos           |      ❌     |      ✔️     |  
| Rapidez                    |      ✔️     |      ✔️     |      

## Notas 📋

- Puedes utilizar otro editor de codigo pero no tendras soporte. se recomienda usar los editores mensionados. 

## Ramas 👾

Ver todas las Ramas [Ramas](https://github.com/BrianMarquez3/Python-Course/settings/branches)

## POO (Programación orientada a objetos)

La programación orientada a objetos (POO, u OOP según sus siglas en inglés) es un paradigma de programación que viene a innovar la forma de obtener resultados. Los objetos manipulan los datos de entrada para la obtención de datos de salida específicos, donde cada objeto ofrece una funcionalidad especial.

- herencia.
- cohesión.
- abstracción.
- polimorfismo.
- acoplamiento.
- encapsulación.

![python](./Images/poo.png)


Muchos de los objetos prediseñados de los lenguajes de programación actuales permiten la agrupación en bibliotecas o librerías, sin embargo, muchos de estos lenguajes permiten al usuario la creación de sus propias bibliote

```
#!/usr/bin/env python3
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        self.mondialLabel = tk.Label(self, text='Hola, Mundo!')
        self.mondialLabel.config(bg="#00ffff")
        self.mondialLabel.grid()
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

if __name__ == '__main__':
    app = Application()
    app.master.title('Aplicación de muestra')
    app.mainloop()
```

Los siguientes son los pasos para crear una aplicación Tkinter junto con la sintaxis:

- Primero, necesitamos importar el módulo Tkinter.
- En segundo lugar, necesitamos crear una ventana de contenedor.
- Luego, agregamos cualquier número de widgets a la ventana del contenedor.
- Por último, aplicamos el activador de eventos en los widgets.

## Interface Grafica (GUI)

### Tkinter

![python](./Images/Tkinter-Grid2.jpg)
<!--![python](./Images/Gui.PNG)-->

El Tkinter módulo ("interfaz Tk") es la interfaz estándar de Python para el kit de herramientas Tk GUI. Tanto Tk como Tkinterestán disponibles en la mayoría de las plataformas Unix, así como en los sistemas Windows. (Tk en sí no es parte de Python; se mantiene en ActiveState).

Ejecutar desde la línea de comando debería abrir una ventana que demuestre una interfaz Tk simple, que le permita saber que está instalado correctamente en su sistema y que también muestre qué versión de Tcl / Tk está instalada, para que pueda leer la documentación específica de Tcl / Tk versión.python -m TkinterTkinter

```
from tkinter import *
```

| Python Tkinter                                               |             |  
|--------------------------------------------------------------|:-----------:|
| Pyhton Tkinter Add ZipCode                                   |      ✔️     |    
| Python Tkinter Add Input Boxes For Our CRM Tool              |      ✔️     |       
| Python Tkinter Adding a Status Bar                           |      ✔️     |          
| Python Tkinter Adding Frames                                 |      ✔️     |      
| Python Tkinter Binding Dropdown Menus and Combo Boxes        |      ✔️     |    
| Python Tkinter Build a Geography Flashcard APP               |      ✔️     |     
| Python Tkinter Build a Weather App                           |      ✔️     |     
| Python Tkinter Build an Imagen Viewer                        |      ✔️     |  
| Python Tkinter Building out Database                         |      ✔️     |  
| Python Tkinter Change Colors Weather App                     |      ✔️     |  
| Python Tkinter Checkboxes                                    |      ✔️     |  
| Python Tkinter Classes                                       |      ✔️     |  
| Python Tkinter Color Picker                                  |      ✔️     |  
| Python Tkinter Create a Database and Table CRM               |      ✔️     |  
| Python Tkinter Create CRM database Tool                      |      ✔️     |  
| Python Tkinter Create New Windows                            |      ✔️     |  
| Python Tkinter Creating Buttons                              |      ✔️     |  
| Python Tkinter Building out Database                         |      ✔️     |  
| Python Tkinter Creating input Fields                         |      ✔️     |  
| Python Tkinter Creating Input fields II                      |      ✔️     |  
| Python Tkinter Delete a Record                               |      ✔️     |  
| Python Tkinter Delete Frame Children Widgets                 |      ✔️     |  
| Python Tkinter Drop Box Database Search CRM                  |      ✔️     |  
| Python Tkinter Dropdown Menus                                |      ✔️     |  
| Python Tkinter Export CRM Database to Excel File             |      ✔️     |  
| Python Tkinter How To Risize Entry Box height                |      ✔️     |  
| Python Tkinter Keyboard Event Binding                        |      ✔️     |  
| Python Tkinter Lookup all CustomersCRM                       |      ✔️     |  
| Python Tkinter Lookup Customer By Last Name CRM              |      ✔️     |  
| Python Tkinter MariaDB                                       |      ✔️     |  
| Python Tkinter Matplolib Charts                              |      ✔️     |  
| Python Tkinter Menu Bars                                     |      ✔️     |  
| Python Tkinter Message Boxes                                 |      ✔️     |  
| Python Tkinter Multiple CRM search Results                   |      ✔️     | 
| Python Tkinter Open Files Dialog Box                         |      ✔️     | 
| Python Tkinter Overwrite Grid Labels                         |      ✔️     | 
| Python Tkinter Paned Windows                                 |      ✔️     | 
| Python Tkinter Positioning                                   |      ✔️     | 
| Python Tkinter Radio Butttons                                |      ✔️     | 
| Python Tkinter Random Winner Generador                       |      ✔️     | 
| Python Tkinter Remove Labels                                 |      ✔️     | 
| Python Tkinter Sliders                                       |      ✔️     | 
| Python Tkinter Standalone EXE Executable                     |      ✔️     | 
| Python Tkinter Unicode Character & Special Characters        |      ✔️     | 
| Python Tkinter Update a Record                               |      ✔️     | 
| Python Tkinter Update a Record II                            |      ✔️     | 
| Python Tkinter Update MariaDb records                        |      ✔️     | 
| Python Tkinter Using Databases                               |      ✔️     | 
| Python Tkinter Using Frames with Menus                       |      ✔️     | 
| Python Tkinter Using Icons, Image                            |      ✔️     | 


## A. I Programming with Python 🤖

Fundamentos esenciales de la IA: las herramientas de programación (Python, NumPy, PyTorch), las matemáticas (cálculo y álgebra lineal) y las técnicas clave de las redes neuronales (descenso de gradiente y propagación hacia atrás).

![python](./Images/python2.jpg)

## Spotify
Music Python [List on Spotify](https://open.spotify.com/playlist/11AwbhmXyh2jKlsHmaxcP9)


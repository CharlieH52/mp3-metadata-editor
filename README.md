<div align="center">

# *MP3 Metadata Editor*

</div>

## Índice

## Introducción
Como parte de un ***"Side Project"*** he creado este editor de metadatos para archivos MP3. Con esta aplicacion puedes editar directamente las etiquetas ***"title"***, ***"artist"***, ***"album"***, ***"date"*** y ***"length"***.

Es una aplicación iterativa, una vez configures las ***.env*** podras editar todos los archivos que haya dentro de la ruta raíz, además es posible pausar el progreso de tu edición, ya que la aplicación crea un archivo ***.ignorefile*** que almacena las rutas que ya has editado con anterioridad, de esta manera evitas editar nuevamente un archivo recientemente editado.

> [!NOTE]  
> Es posible agregar mas campos para editar segun la necesidad e incluso agregar caracteristicas como soportar mas formatos, segun lo que necesites, por lo pronto esto ha solucionado mi problema particular, ya que algunos de mis archivos no cuentan con todos sus metadatos o contienen caracteres raros.
>
> Lo dejo a criterio de quien quiera probar... :blush:

## Dependencias

### [mutagen](https://mutagen-readthedocs-io.translate.goog/en/latest/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc)
Libreria principal para abrir y editar los metadatos de los archivos MP3 con ***mutagen.mp3*** y ***mutagen.easyid3***.

### [flet](https://flet.dev/)
Utilizada para la creación de una interfaz rápidas.

### [python-dotenv](https://pypi.org/project/python-dotenv/)
Necesario para evitar los ***magic-strings***, utiliza variables de entorno.

## Instrucciones

1. Carga el proyecto en **VSCode**
2. Instala dependencias desde **requirements.txt** 
3. Crea el archivo ***.env*** y establece las rutas **absolutas**.

    ```
    MUSIC_BANK = X:\MUSIC  
    IGNORE_FILE = X:\MUSIC\.ignorefile
    ```

4. Ejecuta dese **main.py**

> [!NOTE]
> Automáticamente se creara el archivo ***.ignorefile*** y anexara todos los archivos **.mp3** que haya dentro de la ruta raíz.
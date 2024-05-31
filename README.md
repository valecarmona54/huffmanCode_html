### Aplicación de Compresión de Datos con Algoritmo de Huffman

## Por:
Mayezly Tatiana Gafaro Boada

### Interfaz web:
Juliana Casas Ramírez
Maria Celeste Zuluaga

#### Descripción General
La aplicación permite codificar y decodificar mensajes usando el algoritmo de Huffman. Funciona en consola, Kivy e interfaz web, y utiliza NeonDB para almacenamiento.

#### Objetivo de la Aplicación
Busca ofrecer una herramienta eficiente para reducir el tamaño de textos mediante compresión de datos.

#### Algoritmo de Huffman
Este método de compresión sin pérdida asigna cadenas de bits más cortas a los caracteres más frecuentes, reduciendo el tamaño del archivo sin perder información.

#### Componentes de la Aplicación
1. **Consola**: Interfaz de línea de comandos para codificar y decodificar mensajes.
2. **Kivy**: Interfaz gráfica que facilita la interacción visual con la aplicación.
3. **Interfaz Web**: Accesible desde cualquier navegador para realizar operaciones de compresión y descompresión.

#### Base de Datos NeonDB
NeonDB almacena datos de usuarios y mensajes, asegurando un almacenamiento eficiente y seguro.
#### Funcionalidades Clave
1. **Codificación de Mensajes**: Comprime mensajes y los almacena junto con el árbol de Huffman.
2. **Decodificación de Mensajes**: Decodifica mensajes comprimidos usando el árbol de Huffman.
3. **Gestión de Usuarios**: Permite registro e inicio de sesión, con acceso al historial de mensajes.
4. **Interfaz Gráfica y Web**: Ofrece una experiencia de usuario amigable en diversas plataformas.
5. **Historial de Mensajes**: Almacena y muestra el historial de mensajes codificados y decodificados.

### Prerrequisitos 

Antes de comenzar, asegúrate de tener lo siguiente:

1. **Computadora:** Necesitarás una computadora (Windows, macOS o Linux) para abrir la Calculadora Pensional.

2. **Conexión a Internet:** Asegúrate de tener una conexión a Internet estable para descargar la carpeta "PensionCalculatorProBD-main".

3. **Programa de Extracción de Archivos:** Deberás tener instalado un programa que te permita extraer archivos comprimidos, como WinRAR, 7-Zip o el descompresor integrado en tu sistema operativo.

4. **Espacio en Disco:** Asegúrate de tener suficiente espacio en disco para almacenar y ejecutar la Calculadora Pensional.

5. **Permisos de Ejecución:** Es posible que necesites tener permisos de ejecución para ejecutar el archivo ejecutable "Ejecutable_Calculadora". Si estás utilizando un sistema operativo que requiere permisos de administrador, asegúrate de tenerlos.

6. **Flash:**  Debes instalar flask en tu sistema. Es posible decargarlo utilizando el comando pip install flask en la terminal de tu sistema.

Con estos prerrequisitos, estarás listo/a para abrir y utilizar la interfaz web de  HuffCompresor en tu computadora. ¡Disfruta utilizando el compresor de textos  HuffCompresor!

7. **selenium:**  Debes instalar selenium en tu sistema. Es posible decargarlo utilizando el comando pip install selenium en la terminal de tu sistema.

### Conexión a la base de datos:

1. **Ingresar a la página Neon.Tech**: Abre tu navegador web y accede a la página web de Neon.Tech.

2. **Registro/Inicio de sesión**: Si aún no tienes una cuenta, regístrate en Neon.Tech. Si ya tienes una cuenta, inicia sesión con tus credenciales.

3. **Crear un proyecto**: Una vez que hayas iniciado sesión, dirígete al panel principal y busca la opción para crear un nuevo proyecto. Haz clic en ella y proporciona un título para tu proyecto. Durante este proceso, también podrás nombrar la base de datos, así que ponle el nombre que prefieras, como por ejemplo "BattleShip". Completa los pasos para crear el proyecto.

4. **Ir al Dashboard**: Después de crear el proyecto, serás redirigido al Dashboard o panel de control. Si no eres redirigido automáticamente, busca la opción para acceder al Dashboard desde la página principal de Neon.Tech.

5. **Obtener la cadena de conexión**: En el Dashboard, busca la sección o menú que indique "Connection string". Despliega este menú y elige la opción que dice "Parameters only". Aparecerá un campo de texto con la cadena de conexión.

6. **Copiar la cadena de conexión**: Selecciona y copia todo el contenido que se encuentra en el campo de texto de la cadena de conexión.

7. **Pegar los parámetros en el archivo de configuración**: Ahora, dirígete a la carpeta de tu proyecto en el repositorio. Busca la carpeta llamada "controller". Dentro de esta carpeta, encontrarás un archivo llamado "SecretConfigSample.py". Abre este archivo utilizando un editor de texto.

8. **Pegar los parámetros en el archivo**: Dentro del archivo "SecretConfigSample.py", busca la sección correspondiente a la configuración de la base de datos. Pega los parámetros que copiaste de Neon en el campo correspondiente de este archivo.

9. **Guardar y renombrar el archivo**: Una vez que hayas pegado los parámetros, guarda los cambios en el archivo "SecretConfigSample.py". Luego, cambia el nombre del archivo de "SecretConfigSample.py" a "SecretConfig.py".

Con estos pasos completados, habrás configurado correctamente la conexión a la base de datos en tu proyecto Neon.Tech.

### Creación de tablas.

1. Una vez que hayas iniciado sesión, busca y haz clic en la opción de "SQL Editor" o "Editor SQL". Esta opción generalmente se encuentra en el panel de administración o en el menú de herramientas.

2. Se abrirá una nueva ventana o pestaña donde podrás ingresar y ejecutar comandos SQL en tu base de datos NeonDB.

3. Abre tu editor de texto preferido en tu computadora.

4. Copia los comandos SQL del archivo `crear_historial.sql` y `crear_usuarios.sql` que se encuentran en la carpeta `sql` de tu proyecto `huffmanCode_html`.

5. Pega los comandos SQL copiados en el editor de texto.

6. Revisa los comandos SQL para asegurarte de que estén correctos y no haya errores.

7. Una vez verificados, copia los comandos SQL desde tu editor de texto.

8. Regresa a la ventana o pestaña del "SQL Editor" en la página de Neon Tech.

9. En el "SQL Editor", pega los comandos SQL que copiaste en el paso anterior en el área de texto proporcionada para escribir consultas SQL.

10. Después de pegar los comandos SQL, busca y haz clic en el botón para ejecutar las consultas SQL. Este botón podría tener una etiqueta como "Ejecutar", "Run" o un icono de flecha hacia la derecha.

11. Espera a que las consultas SQL se ejecuten. Deberías ver mensajes de éxito si las consultas se ejecutan correctamente.

12. Verifica que las tablas se hayan creado correctamente revisando la estructura de la base de datos o ejecutando consultas de muestra para recuperar datos de las tablas recién creadas.

Siguiendo estos pasos, podrás insertar las tablas necesarias en tu base de datos NeonDB utilizando el "SQL Editor" en la página de Neon Tech.

### Ejecución:
# Paso a paso  desde la terminal para ejecutar la interfaz web:

# Opción 1: Descargar la carpeta comprimida
1. Descarga la carpeta comprimida `huffmanCode_html` desde GitHub y guárdala en tu computadora.

2. Descomprime la carpeta `huffmanCode_html` en una ubicación de tu elección.

3. Abre la terminal en tu sistema operativo. Puedes hacerlo buscando "terminal" en el menú de inicio (en el caso de Windows) o utilizando la aplicación Terminal (en el caso de macOS o Linux).

4. Utiliza el comando `cd` seguido de la ruta de la carpeta `huffmanCode_html` en tu sistema. Por ejemplo:
   ```
   cd ruta/de/la/carpeta/huffmanCode-copia
   ```
 5. Ahora estás en la ubicación donde se encuentra el archivo `app.py`. Para ejecutarlo, utiliza el siguiente comando:
   ```
   python app.py
   ```
6. Presiona Enter para ejecutar el comando. Aparecerá un mensaje similar a este:
     ```
     * Running on http://127.0.0.1:5000
     Press CTRL+C to quit
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 501-583-688
     ```
7. Copia el enlace de "Running on" (en este caso, `http://127.0.0.1:5000`) y pégalo en tu navegador, o presiona Shift y haz clic en el enlace para seguirlo directamente.
Ahora podrás acceder a tu aplicación web en el navegador utilizando la dirección proporcionada.

Con estos pasos, estarás ejecutando el archivo `app.py` desde la terminal y poniendo en marcha tu aplicación web. 

**Opción 2: Clonar el Repositorio desde Github:**

1. **Clonar el Repositorio desde Github:**
   - Abre la terminal o línea de comandos en tu computadora.
   - Navega hasta el directorio donde deseas clonar el repositorio utilizando el comando cd.
   - Utiliza el siguiente comando para clonar el repositorio desde GitHub:

   git clone https://github.com/usuario/huffmancode_html.git

   Reemplaza usuario por el nombre de usuario de GitHub donde se encuentra el repositorio.

**Clonar el repositorio desde la terminal:**
   - Abre la terminal o línea de comandos en tu computadora.
   - Navega hasta el directorio donde deseas clonar el repositorio utilizando el comando `cd`.
   - Ve a la página del repositorio en GitHub que deseas clonar.
   - Haz clic en el botón verde que dice **Code**.
   - Copia la URL que aparece en el menú desplegable (debería tener el formato `https://github.com/usuario/repositorio.git`).
   - Utiliza el siguiente comando en tu terminal para clonar el repositorio, pegando la URL que copiaste:

     ```bash
     git clone https://github.com/usuario/huffmancode_html.git
     ```
Ahora habrás clonado el repositorio en tu máquina local y podrás comenzar a trabajar con él.

## Ejecutar el Archivo app.py:
Ahora estás en la ubicación donde se encuentra el archivo `app.py`. Para ejecutarlo, utiliza el siguiente comando:
   ```
   python app.py
   ```
   - Presiona Enter para ejecutar el comando. Aparecerá un mensaje similar a este:
     ```
     * Running on http://127.0.0.1:5000
     Press CTRL+C to quit
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 501-583-688
     ```
   - Copia el enlace de "Running on" (en este caso, `http://127.0.0.1:5000`) y pégalo en tu navegador, o presiona Shift y haz clic en el enlace para seguirlo directamente.
Ahora podrás acceder a tu aplicación web en el navegador utilizando la dirección proporcionada.
Gracias por la corrección. Aquí está la guía actualizada:

### Ejecutar los Tests


1. Abre la terminal en tu computadora.
2. Utiliza el comando `cd` seguido de la ruta completa hacia la carpeta `huffmanCode_html`. Por ejemplo, si la carpeta `huffmanCode_html` está en el directorio `/Users/tu_usuario/Documentos`, puedes hacerlo así:
   ```
   cd /Users/tu_usuario/Documentos/huffmanCode_html
   ```
3. Una vez dentro de la carpeta `huffmanCode_html`, usa el comando `cd` para ingresar a la carpeta `tests`:
   ```
   cd tests
   ```

Ahora estarás dentro de la carpeta `tests` y podrás ejecutar los archivos de prueba según sea necesario. 

# Ejecución de `Test_final.py`

 Ejecuta el comando `python Test_final.py` desde esta ubicación.

- Uso del código fuente Huffman por consola: Para hacer uso de la aplicación por consola se debe correr el archivo console.py que se encuentra en la carpeta 'consoleHuffman'.
    - Para ejecutarlo por la terminal se debe especificar la ruta de busqueda donde se encuentran los módulos, además de:
      python huffmanCode\src\view-console\console.py

    - Recuerde que la base de datos unicamente esta conectada a la interfaz por consola. 

- Uso del Kivy: Para hacer uso de la aplicación con interfaz gráfica se debe correr el archivo interfaz.py que se encuentra en la carpeta 'interfazHuffman'.
    - Para ejecutarlo por la terminal se debe especificar la ruta de busqueda donde se encuentran los módulos, además de:
      python huffmanCode\src\view-gui\huffman_gui.py

- Uso de las pruebas unitarias: Para hacer uso de las pruebas unitarias de la base de datos debe correr el archivo TestMVC.py que se encuentra en la carpeta 'tests'.
    - Para ejecutarlo por la terminar debe especificar la ruta de busqueda donde se encuentran los módulos, ademas de :
      python huffmanCode\tests\TestMVC.py
      

## Ejecutar pruebas unitarias
Abra la terminal en su computadora.
En la terminal utilice el comando cd para entrar al escritorio; "cd Escritorio" (depende del nombre que tenga su escritorio o que ruta tiene para llegar a este).
Utilice el mismo comando para entrar a la aplicación "cd Interfaz_Web_Batalla_Naval-main".
Utilice el mismo comando "cd" para ingresar a la carpeta test, "cd test"
Despues utilice el comando "python Test.py".
Una vez ejecutado el comando anterior podras observar el resultado de las pruebas unitarias.

# Bibliotecas Utilizadas:
El proyecto hace uso de las siguientes bibliotecas estándar de Python:

unittest: Utilizada para escribir y ejecutar pruebas unitarias.

Dependencias de Otros Proyectos:
El proyecto no tiene dependencias externas a otros proyectos. Todas las funcionalidades están implementadas dentro del propio proyecto sin requerir bibliotecas externas.
# Guía para Instalar psycopg2 en tu Sistema
 Instale psycopg2:
 *Abre tu terminal:* Si estás en Windows, abre el símbolo del sistema o PowerShell. En macOS o Linux, abre la terminal.

 *Instala pip si no lo tienes:* Si no tienes pip instalado, puedes instalarlo ejecutando el siguiente comando en la terminal:
   
   python -m ensurepip --default-pip
   
*Instala psycopg2:* Usa pip para instalar psycopg2 ejecutando el siguiente comando en la terminal:
   
   pip install psycopg2
   
 *Espera a que termine la instalación:* pip descargará e instalará psycopg2 y todas las dependencias necesarias. Espera a que termine el proceso.

*Verifica la instalación:* Después de que la instalación se complete, puedes verificar que psycopg2 esté instalado correctamente ejecutando el siguiente comando en la terminal:
   
   pip show psycopg2
   
 *¡Listo para usar!:* Ahora puedes importar psycopg2 en tus scripts de Python y utilizarlo para conectarte y trabajar con bases de datos PostgreSQL.

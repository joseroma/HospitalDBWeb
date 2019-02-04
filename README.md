# HospitalDBWeb

Hemos decidido estructurar este proyecto en 3 bloques.

#### Base de datos:

Aquí encontramos todo el código utilizado y los resultados obtenidos para generar la base de datos. Encontramos dos ficheros.

- **Generate_BD_data**: A partir de unas bases de datos de *Kaggle* (que se encuentran en la carpeta `internet_data_sets`) hemos rellenado con datos aleatorios (con el script `DataGenerator-conFK.py`) una base de datos en MySQL. Las tablas que subimos a MySQL las podemos encontrar en la carpeta `generated_tables` (contiene los *.csv* con las tablas y datos usados.).

- **MySQL**: Dentro de esta carpeta podemos encontrar los scripts de creación y copia de seguridad de la base de datos que hemos creado.

#### HL7:

Servicio socket que permite enviar mensajes codificados en HL7. Podemos ver dos carpetas: `receivedData` y `sendData` que simplemente utilizaremos para guardar los archivos que se envían y reciben.

- **client.py**: Cliente.
- **server.py**: Servidor.
- **HL7encoder**: Aquí encontramos una función para codificar el mensaje HL7.

#### XML:

- **mydbSchema**: Schema del XML, indica la estructura de arbol que deberán tener los datos del XML y sus formatos entre otras restrincciones, si funciona al linkarlo, significará que el XML es correcto.

- **mydbXSLT**: XSLT para visualizar el XML con HTML en la web. Indica las columnas y los datos que apareceran en cada tabla apuntando a su ruta correspondiente en el arbol definido en Schema.

- **CLData_Output.xml**: XML creado a partir del script *sql_2_xml*, linkado con el esquema y XSLT , por lo que se peude abrir directamente con un explorador y visualizar las tablas con los datos y estructura del schema.

- **style.css**: Hoja de estilos
  


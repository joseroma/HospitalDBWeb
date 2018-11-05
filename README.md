# HospitalDBWeb

#### Code:

- db_generator: A partir de unas bases de datos de *Kaggle*, cogemos algunas columnas y otras las generamos, creando el contenido de las tablas de nuestra base de datos.

- sql_2_xml: Usando el paquete `lxml.etree` indicamos la estructura de arbol que tendrá nuestro XML con la función `SubElement` y los datos correspondientes a cada columna de las tablas, creando así archivo XML desde nuestra DB.

#### MySQL:

- create.sql: script de creación de la BD en MySQL.
- est.mwb: modelo de la BD.

#### XML:

- mydbSchema: Schema del XML, indica la estructura de arbol que deberán tener los datos del XML y sus formatos entre otras restrincciones, si funciona al linkarlo, significará que el XML es correcto.

- mydbXSLT: XSLT para visualizar el XML con HTML en la web. Indica las columnas y los datos que apareceran en cada tabla apuntando a su ruta correspondiente en el arbol definido en Schema.


- CLData_Output.xml: XML creado a partir del script *sql_2_xml*, linkado con el esquema y XSLT , por lo que se peude abrir directamente con un explorador y visualizar las tablas con los datos y estructura del schema.

#### datasets: 

- Results_datasets_withoutFK contiene los *.csv* con las tablas y datos usados.


  


# SH4R1NG4N

Video comentando un poco las caracteristicas del programa a unos amigos:
https://youtu.be/Eqqy3Z9a-W4

![alt text](https://github.com/NicolasMuras/SH4R1NG4N/blob/master/Images/hud_sharingan.jpg?raw=true)

SH4R1NG4N Es una plataforma diseñada para trabajar con informacion y bases de datos.
Cuenta con scripts que nos ayudaran a:
- Recolectar informacion de perfiles de Facebook rapidamente mediente web scraping.
- Analizar, transformar la informacion recolectada y almacenarla en una base de datos.
- Generar diccionarios para "brute-force attacks" a partir de nuestra base de datos.
- Manejo comodo de la informacion.

PROXIMAMENTE:
- Mapa satellital donde poder visualizar los puntos de interes recolectados.

INSTALACION:
Asegurarse de tener instalado chrome para utilizar el webscraper (script_izanami).
Compilar y ejecutar.
Funcionando en linux

ESTRUCTURA DE SHARINGAN
GENERAL:
* Sistema de barras de progreso (0-100%) que muestre la situacion de los procesos en tiempo real.
* Boton para matar el proceso seleccionado.
* Modalidad para camuflar la GUI y transformarla en otra GUI por ejemplo Word.
 / Luz que se enciende para verificar conexion a la database.
 / Hacer que al settear la configuracion de la base de datos ejecute "SHOW TABLES".
 / Atras y adelante en los comandos SQL con CTRL+Q/CTRL+W.
 / Boton para desplegar toda la informacion del ID actual.
 / Boton para desplegar la info de NET del ID actual.
* Boton para desplegar las notas del ID actual.
* Sistema de frames, que muestre la cantidad de datos de un grupo de entradas de la DB, y permita acceder rapido a ellos.
* Botones < > para navegar por frames y boton para añadir una entrada a la DB manualmente.
* Configuraciones avanzadas: Tor, Proxy, Time (programar un ataque por fecha y hora).
* Mostrar el uso del CPU en un medidor.
* MODULOS SH4R1NG4N:
	- MAP: Mapa satelital de la ciudad donde se muestran los perfiles con datos de ubicacion.
	- SHELL: Shell para ejecutar comandos/Manejar reverse_shells u otros scripts desde SH4R1NG4N.
	- MITM: Entradas del trafico y sniffer de paquetes de la red afectada.
	- KEYLOG: Entradas de keyloggers de los equipos infectados.
	- BOTNET: Mapa grafico de los equipos infectados pertenecientes a la botnet.
	- LOG: Errores en bruto y otra info del programa.
* Agregar botones dinamicos para las opciones de los modulos.
* Sistema de control de camaras de vigilancia.
* Zoom al hacer click en la imagen de perfil.
* Limpiar informacion extra de la GUI (codigo irrelevante)


IZANAMI:
* Hacer que descarge la foto de perfil en grande y pequeño.
* Hacer que cuando un escaneo termine se guarde en la DB.
* IZANAMI Modules:
	- React: Descarga las 30 publicaciones mas recientes.
	- Family: Busca en sus amigos personas con el mismo apellido, descarga en HTML la pagina principal y la de info de cada uno.
	- Multimedia: Descarga los HTML de las fotos y videos, con el fin de encontrar etiquetados y procesar luego la info de comentarios.


IZANAGI:
* Terminar con las expresiones regulares.
* Procesar los modulos de IZANAMI, para extraer datos:
	- React: Cuenta las reacciones por persona de las publicaciones descargadas. Analiza comentarios en busca de palabras clave.
	- Family: Mediante expresiones regulares procesa la informacion de los HTML descargados de family, agrega a DB la info.
	- Multimedia: Saca de las fotos y videos a personas etiquetadas, analiza los comentarios con palabras clave.
	- Friends: Determina las personas que mas reaccionan mediante React/Family, determina relaciones de familia o amistad,
	  descarga el HTML de la pagina principal/info de cada amigo y familiar, luego agrega las entradas y su info a la base de datos. 


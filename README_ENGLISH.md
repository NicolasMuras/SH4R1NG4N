# SH4R1NG4N
In progress...

A video commenting the characteristics of the program to some friends (IN SPANISH):
https://youtu.be/Eqqy3Z9a-W4

![alt text](https://github.com/NicolasMuras/SH4R1NG4N/blob/master/Images/hud_sharingan.jpg?raw=true)

SH4R1NG4N Is a platform designed to work with information and databases.
Count with scripts that will help us to:
- Recolect facebook profiles information through web scraping.
- Analize, transform the recolected information and save it in a database.
- Dictionary generation for "brute-force attacks" from our database.
- Comfortable handling of the information.

NEXT TO DO:
- Satellital map where the view the points of view recolected.
- Mode to camouflage the GUI and make it similar to another GUI like Word Office (for example).

INSTALATION:
Make sure that you have chrome installed to work with the webscraper (script_izanami).
Compile and execute.
Working on linux.

SH4R1NG4N FUNCTIONS:
GENERAL:
* Progress bar system (0-100%) to show the situation of the process in real time.
* Button for manage the selected process.
 / Light that comes on to verify that the connection with the database is successful.
 / When you connect sucessfully with the database the command "SHOW TABLES" is executed.
 / Back and forward steps (SQL commands) with CTRL+Q/CTRL+W.
 / Button to display all information about the actual ID.
 / Button to display all NET information about the actual ID.
* Button to display notes of the actual ID.
* "Frame system", that shows the quantity of data about a group of entries in the DB, and allow a rapid access to them.
* Buttons < > to navigate through frames and button to add a entry manually in the DB.
* Advanced configurations: Tor, Proxy, Time (program and attack with date and hour given).
* Shows the CPU use in a meter.
* SH4R1NG4N MODULES:
	- MAP: Satellital map of the city where the profiles with location data are displayed.
	- SHELL: Simple shell to execute commands/Manage reverse_shells and other scrips from SH4R1NG4N.
	- MITM: Traffic entries and sniffing of the communication of the affected network.
	- KEYLOG: Keyloggers entries of the affected machines.
	- BOTNET: Grafic map of the infected machines that belong to our botnet.
	- LOG: Gross erros and other info of the program.
* Add dynamic buttons for the options of the modules.
* Camera system control module.
* Zoom when we clicked the profile image.
* Clean irrelevant code in the GUI file.


IZANAMI:
* Download the facebook profile photo in small and big.
* When scan is finished it save the info in the DB.
* IZANAMI Modules:
	- React: Download the 30th more recent publications.
	- Family: Find in the profile friends, targets with the same lastname, download in a HTML file the main page and the information of each one
	- Multimedia: Download the HTML of the photos and videos, with the objective of find labels for after processing of the info and comments.

IZANAGI:
* Regular expressions.
* Extrac data from the IZANAMI modules:
  - React: Counts the reactions for each person of the downloaded publications. Analyze the comments in search of key words.
  - Family: Through regular expressions, process the information of the downloaded HTML files of "family", and adds the info to the DB.
	- Multimedia: Collects profiles from the downloaded videos and photos, analyze the comments with key word.
	- Friends: Determine the people who react the most to posts React/Family, Determine family and friends relations,
	  download the main HTML file/info of each friend and familiar, next to it adds the entries and their info to the database. 



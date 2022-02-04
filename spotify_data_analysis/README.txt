ACTIVITAT 4
----------------------------------------------------------------
Realització de projecte per a UOC Sound Dynamics  per crear una aplicació per descobrir artistes musicals. 
Aquest paquet de Python llegeix les dades, les prepara per l’anàlisi,calcula algunes
estadístiques bàsiques, i crea visualitzacions per comparar diferents artistes.
Les dades que s’utilitzaran en l’anàlisi contenen informació sobre cançons, sobre els àlbums
que les contenen, i sobre els artistes que les han creat. A part de detalls bàsics com per
exemple, el nom dels artistes o el títol de les cançons, les dades més interessants que
seran la base de l’anàlisi són les audio features que ens proporciona Spotify.
---------------------------------------------------------------------
Qué conté aquest paquet?
---------------------------------------------------------------------
Aquest paquet conté els següents arxius.
	- utils.py Conté codi de funcionalitat general
	- plots.py Conté codi per crear les gràfiques
	- main.py L'arxiu principal el qual executarem a la consola
	- carpeta tests En aquesta carpeta estan els unitests del codi anterior
---------------------------------------------------------------------
Pre-requisits
--------------------------------------------------------------------
El software necessari per a funcionar està a l'arxiu requeriments.txt
---------------------------------------------------------------------
Com executar aquest projecte
---------------------------------------------------------------------
Per fer funcionar aquest projecte hem de seguir els següents passos:
	1- Descomprimir el projecte a la carpeta HOME
	2- Executar en la consola el següent codi --> python3 main.py
Per a què el codi funcione haurem de tindre una carpeta data amb el següent arxiu:
	- data.zip
---------------------------------------------------------------------
Com executar els tests
---------------------------------------------------------------------
Els tests es poden executar amb el següent codi:
python3 -m unittest discover -s tests/
---------------------------------------------------------------------
Tests Coverage
---------------------------------------------------------------------
Es pot utlitzar l'eina coverage.py per veure quina cobertura del codi ha sigut testejada
S'ha d'executar el següent codi:
coverage run --source=. -m unittest discover -s tests/
coverage report
---------------------------------------------------------------------
Autoria
---------------------------------------------------------------------
Aquest projecte ha sigut desenvolupat per Joan Miquel Alfonso Garcia
---------------------------------------------------------------------
Llicència
---------------------------------------------------------------------
Aquesta informació està present a license.txt
---------------------------------------------------------------------
Bibiliografia
---------------------------------------------------------------------
Per fer aquest projecte s'han consultat les següents fonts:
- Unitat 0,1,2,3,4,5 i 6 dels recursos de Programació per a la ciència de dades
- https://stackoverflow.com/questions/5478351/python-time-measure-function
- https://thispointer.com/python-read-a-csv-file-line-by-line-with-or-without-header/
- https://www.geeksforgeeks.org/how-to-merge-two-csv-files-by-specific-column-using-pandas-in-python/
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
- https://stackoverflow.com/questions/31789160/convert-select-columns-in-pandas-dataframe-to-numpy-array
- https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory
- https://stackoverflow.com/questions/39141856/capitalize-first-letter-of-each-word-in-a-dataframe-column
- https://www.geeksforgeeks.org/how-to-fill-nan-values-with-mean-in-pandas/
- https://www.dataquest.io/blog/python-api-tutorial/
- https://stackoverflow.com/questions/12934699/selecting-fields-from-json-output

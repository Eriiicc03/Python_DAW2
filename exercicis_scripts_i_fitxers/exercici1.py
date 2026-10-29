""" 
1- Crea un script que busqui una paraula dins d'un fitxer de text. Ha de mostrar la quantitat de vegades que ha trobat la paraula.
Ha d'admetre les següents opcions:
-f o --fitxer amb el nom del fitxer.
-p o --paraula amb la paraula que volem trobar.
--help o -h mostra un missatge informatiu del funcionament.
Ha de detectar correctament les opcions i paràmetres i mostrar-ne un missatge en cas de dades errònies. Si hi ha diverses opcions, les ha de gestionar totes.
S’ha de fer print, des del main, dels resultats retornats per les funcions.

"""

import sys

def fitxer():
    return
    
def paraula():
    return
    
def help():
    return
#try:
if sys.argv[1] == '-f' or sys.argv[1] == '--fitxer':
    print ("HOla")
if sys.argv[1] == '-p' or sys.argv[1] == '--paraula':
    print ("HOla")
if sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print ("Ayuda.")
#except IndexError:
#    print("Aquesta opció no existeix.")

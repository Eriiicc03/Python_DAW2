""" 
2- Crea un mètode concatena, que a partir de dos fitxers, afegeixi el contingut del segon fitxer al primer fitxer. 
Si el segon fitxer no és vàlid, ha de mostrar un missatge informatiu.
"""

import os
import exercici1


def concatena(nomFitxer, nomFitxer2):
    if os.path.isfile(nomFitxer2):
        with open(nomFitxer2, 'r', encoding='utf-8') as origen:
            with open (nomFitxer, 'a', encoding='utf-8') as desti:
                desti.write(origen.read())


    else: 
        print("No es valid")
    
if __name__ == '__main__':
    concatena('fitxer.txt', 'fitxer2.txt')     # 1. junta fitxer2 al final de fitxer
    exercici1.mostra('fitxer.txt')             # 2. enseña cómo ha quedado
    concatena('fitxer.txt', 'novalid.txt')     # 3. prueba el caso no válido
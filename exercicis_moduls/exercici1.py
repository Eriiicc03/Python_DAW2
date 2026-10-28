"""
1- Crea un script per realitzar còpia de seguretat de diversos orígens.

Farà falta una funció per a fer la còpia d'un origen a un destí.

def copiaDades(origen, desti): # Còpia l'origen amb tot el seu contingut a destí.

L'script tindrà una variable amb la llista d'orígens que s'han de copiar i una altra variable amb el destí de les còpies.

origens=['/home/usuari/', '/root/', '/etc/', '/dades/']  # Fan falta drets de lectura

desti='/copies/'  # Fan falta drets d'escriptura

S'ha de fer un bucle per recorrer la llista origens i fer la còpia de cada un.

Funcions útils:

os.path.join(path, path2, ...)  EX:  nom=os.path.join("/info/",  desti)
shutil.copytree(src, dst,  dirs_exist_ok=True)
shutil.copy2(src, dst)
os.makedirs(os.path.dirname(desti), exist_ok=True)
os.path.isdir(path)
"""

import os
import shutil

#origens=['/DAW2/proves/origen1','/DAW2/proves/origen2', '/DAW2/proves/fitxer.txt', '/DAW2/imatges']
#desti = '/DAW2/copies'

origens=['/home/eriiicc03/Documentos/DAW2/MP01 - Programació amb Frameworks/RA1. Python/DAW2/proves/origen1','/home/eriiicc03/Documentos/DAW2/MP01 - Programació amb Frameworks/RA1. Python/DAW2/proves/origen2', '/home/eriiicc03/Documentos/DAW2/MP01 - Programació amb Frameworks/RA1. Python/DAW2/proves/fitxer.txt', '/DAW2/imatges']
desti = '/home/eriiicc03/Documentos/DAW2/MP01 - Programació amb Frameworks/RA1. Python/DAW2/copies'


def copiaDades(origen, desti):
    nom = os.path.basename(origen)
    copia = os.path.join(desti, nom)
    if os.path.isdir(origen):
        print(f"Es un directori: {origen}", desti)
        print(copia)
        shutil.copytree(origen,copia, dirs_exist_ok=True)
        
    elif os.path.isfile(origen): 
        print(f"Es un arxiu: {origen}", desti)
        print(copia)
        
        os.makedirs(os.path.dirname(copia), exist_ok=True)
        shutil.copy2(origen, copia)

        
    else:
        print(f"No existeix: {origen}")
        
    
    
if __name__ == '__main__':
    for recorre in origens:
        copiaDades(recorre,desti)


"""
3- Modifica els scripts per permetre tenir diverses còpies. Es tracta d'afegir una variable amb la quantitat de còpies a conservar. S'hauran de crear diversos directoris amb les còpies.
S'han de conservar la quantitat de còpies indicades, sempre les últimes n còpies fetes. En fer la restauració farà falta saber quina és la còpia que volem restaurar.
Exemple:
desti='/home/dades/copies/'
ncopies=5

Això crearia:

/home
  |
  --dades
     |
     --copies
        |
        --1
        |
        --2
        |
        --3
        |
        --4
        |
        --5
 

Si ja hem completat totes les possibles còpies i en volem fer una més, s'haurà de sobreescriure la més antiga.

Funcions útils:

os.path.getmtime(path)
os.path.isdir(path)
 

"""

import os
import shutil
import exercici1

#origen = '/home/eriiicc03/Documentos/DAW2/MP01 - Programació amb Frameworks/RA1. Python/DAW2/proves/fitxer.txt'
#desti = '/home/eriiicc03/Documentos/DAW2/MP01 - Programació amb Frameworks/RA1. Python/DAW2/copies'
origens = ['/DAW2/proves/origen1', '/DAW2/proves/origen2', '/DAW2/proves/fitxer.txt']
desti = '/DAW2/copies3'
ncopies = 3
destiRestaurar = '/DAW2/restaurat'


def escullCarpeta(desti, ncopies):
    # 1. Busquem la primera carpeta lliure
    for element in range(1, ncopies + 1):
        copia = os.path.join(desti, str(element))
        if not os.path.isdir(copia):
            return copia

    # 2. Si no n'hi ha cap de lliure, busquem la més antiga
    rutaMesAntiga = os.path.join(desti, "1")
    tempsMesAntic = os.path.getmtime(rutaMesAntiga)
    for element in range(1, ncopies + 1):
        copia = os.path.join(desti, str(element))
        if os.path.getmtime(copia) < tempsMesAntic:
            rutaMesAntiga = copia
            tempsMesAntic = os.path.getmtime(copia)
    return rutaMesAntiga


def fesCopia(origens, desti, ncopies):
    carpeta = escullCarpeta(desti, ncopies)
    if os.path.isdir(carpeta):
        shutil.rmtree(carpeta)
    os.makedirs(carpeta)
    print("Fent la còpia a:", carpeta)
    for origen in origens:
        exercici1.copiaDades(origen, carpeta)


def restauraCopia(desti, numCopia, destiRestaurar):
    carpeta = os.path.join(desti, str(numCopia))
    if os.path.isdir(carpeta):
        print("Restaurant la còpia:", carpeta)
        llista = os.listdir(carpeta)
        for element in llista:
            ruta = os.path.join(carpeta, element)
            exercici1.copiaDades(ruta, destiRestaurar)
    else:
        print("No existeix la còpia", numCopia)


if __name__ == '__main__':
    opcio = input("1 = Fer còpia, 2 = Restaurar: ")
    if opcio == "1":
        fesCopia(origens, desti, ncopies)
    elif opcio == "2":
        numCopia = int(input(f"Quina còpia vols restaurar (1-{ncopies})? "))
        restauraCopia(desti, numCopia, destiRestaurar)
    else:
        print("Opció no vàlida")

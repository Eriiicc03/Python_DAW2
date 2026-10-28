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
import exercici1
origen = '/home/eriiicc03/Documentos/DAW2/MP01 - Programació amb Frameworks/RA1. Python/DAW2/proves/fitxer.txt'
desti = '/home/eriiicc03/Documentos/DAW2/MP01 - Programació amb Frameworks/RA1. Python/DAW2/copies'

ncopies = 3

exercici1.copiaDades(origen, desti)   
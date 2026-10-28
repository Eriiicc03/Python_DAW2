"""
2- Crea un script per realitzar la restauració de la còpia de seguretat anterior.

L'script tindrà dues variables: origen de les còpies i destí de restauració.

copies='/copies/'  # Fan falta drets de lectura

desti='/proves/'  # Fan falta drets d'escriptura

Funcions útils:

os.listdir(path)  Ex:  llista=os.listdir('/copies')
"""

import os
import exercici1
desti='/DAW2/restaurat'

copies = '/DAW2/copies'

if __name__ == '__main__':
    
    llista=os.listdir(copies)
    for element in llista:
        ruta = os.path.join(copies, element)
        exercici1.copiaDades(ruta,desti)
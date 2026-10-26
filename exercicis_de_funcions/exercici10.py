""" 
10-Crea una funció comptaLES que a partir d'una frase retorni la quantitat de LES trobades.
No es diferencia entre majúscules i minúscules. No s'ha de fer servir el mètode count.
Exemple:
Ell es passa totes les tardes cantant LaLESlesla...
Retorna 3
"""

def comptaLES(frase):
    fraseMinus = frase.lower()
    comptador = 0
    for i in range(len(fraseMinus)):
        if fraseMinus[i] == "l":
            if fraseMinus[i+1] == "e":
                if fraseMinus[i+2] == "s":
                    comptador += 1
    return comptador

frase = input("Introdueix una frase: ")

print(comptaLES(frase))
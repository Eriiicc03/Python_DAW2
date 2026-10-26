"""
9-Crea una funció comptaLA que a partir d'una frase retorni la quantitat de LA trobades.
No es diferencia entre majúscules i minúscules. No s'ha de fer servir el mètode count.
Exemple:
Ell s'ha passat la tarda cantant La, LA, lA, ...
Retorna 4

Exemple:
Ell s'ha passat la tarda cantant LaLAlA, ...
Retorna 4
"""

def comptaLA(frase):
    fraseMinus = frase.lower()
    comptador = 0
    for i in range(len(fraseMinus)):
        if fraseMinus[i] == "l":
            if fraseMinus[i+1] == "a":
                comptador += 1
    return comptador

frase = input("Introdueix una frase: ")

print(comptaLA(frase))
"""
6- Escriu una funció esvocal que a partir un caràcter torni True si el caràcter és una vocal o 
False en cas contrari.


if esvocal(caracter):
    print(caracter, “és una vocal”)
else:
    print(caracter, “NO és una vocal”)
"""

def esvocal(caracter):
    llistaVocals = [a,e,i,o,u]
    for lletra in llistaVocals:
        if caracter in llistaVocals:
            return True
        else:
            return False

caracter = input("Introdueix un caracter: ").lower()


if esvocal(caracter):
    print (caracter, "és una vocal")
else:
    print (caracter, "NO és una vocal")
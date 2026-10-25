"""
8-Crea una funció diferencies que a partir de dues cadenes de text gairebé iguals, retorneu les diferències.
La funció ha de trobar les diferències a la segona cadena i retornar-les en format llista.
Les dues cadenes de text han de ser iguals en longitud.
Exemples:
Em dic mouredev / Em dic meuredov -> ["e", "o"]
Em dic.Brais Moure / Em dic brais moure -> [" ", "b", "m"]
"""

def diferencies(cadena1, cadena2):
    dif = []
    for i in range(len(cadena1)):
        if cadena1[i] != cadena2[i]:
            dif.append(cadena2[i])
    return dif

cadena1 = "Em dic mouredev"
cadena2 = "Em dic meuredov"

print(diferencies(cadena1, cadena2))
"""
1-Crea una llista de valors numèrics enters, no fa falta llegir-la del teclat.
Mitjançant un bucle crea una segona llista, igual a l’anterior, però modificant tots els valors negatius per el seu valor en positiu. Mostra les dues llistes per consola.
Exemple:
Llista 1: [45, -6, 0, -32, 23, 9]
Resultat:
Llista 1: [45, -6, 0, -32, 23, 9]
Llista 2: [45, 6, 0, 32, 23, 9]
"""

Llista1 = [45, -6, 0, -32, 23, 9]

Llista2 = []
aux = 0
for num in Llista1:
    if num < 0:
        aux = num * -1
        Llista2.append(aux)
    else:
        Llista2.append(num)

print(Llista1)

print(Llista2)
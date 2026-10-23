"""
2-Crea una llista de valors numèrics enters, no fa falta llegir-la del teclat.
Mostra per consola els valors de la llista sense repetir cap. Fes servir un bucle i un tipus set.
Exemple:
Llista: [45, -6, 0, -32, -6, 0, 45, 45, 23, 9]
Resultat:
Llista: [45, -6, 0, -32, -6, 0, 45, 45, 23, 9]
Sense repetits: -32 -6 0 45 23 9
"""


Llista = [45, -6, 0, -32, -6, 0, 45, 45, 23, 9]


LlistaNoRepetits = set()

aux = 0

for num in Llista:
    LlistaNoRepetits.add(num)


print(Llista)
print(LlistaNoRepetits)
"""2-Igual a l’exercici 1, però sense permetre noms repetits.

Exemple:

Entra quantitat: 4

nom 1 ? Mortadelo

nom 2 ? Anacleto

nom 3 ? Mortadelo

Repetit, nom 3 ? Sacarino

nom 4 ? Filemón

Els noms són: Mortadelo Anacleto Filemón Sacarino"""

quantitat = int(input("Entra quantitat: "))
llistaNoms = []
contador = 1
while (contador-1) < quantitat:
    nom = input(f"Nom {contador}: ")
    if nom not in llistaNoms:
        llistaNoms.append(nom)
        contador += 1

    else:
        print("Repetit")

    


print(llistaNoms)
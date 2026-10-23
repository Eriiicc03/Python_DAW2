"""1-Demana per teclat una quantitat i a continuació entra per teclat diversos noms fins a la quantitat entrada. 
Al final mostra tots els noms per pantalla.

Exemple:

Entra quantitat: 4

nom 1 ? Mortadelo

nom 2 ? Anacleto

nom 3 ? Mortadelo

nom 4 ? Filemón"""


quantitat = int(input("Entra quantitat: "))
llistaNoms = []
contador = 1
while (contador-1) < quantitat:
    nom = input(f"Nom {contador}: ")
    llistaNoms.append(nom)
    contador += 1

print(llistaNoms)
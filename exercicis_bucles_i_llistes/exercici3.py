""" 
3-Crea una llista amb contingut de tipus str, amb diverses paraules.
Mostra les paraules començant per l’inici de la llista i començant pel final.
Utilitza bucles.
Exemple:
Llista: ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
Resultat:
the quick brown fox jumps over the lazy dog
dog lazy the over jumps fox brown quick the
"""


llistaParaules = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]


llistaReves = []
for i in range (len(llistaParaules) -1, -1, -1):
    print(llistaParaules[i], end=" ")
    
print("")
for i in range(0, len(llistaParaules)):
    print(llistaParaules[i], end= " ")
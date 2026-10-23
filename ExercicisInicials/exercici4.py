"""
4-Crea una llista (list) de diccionaris com els de l’exercici 3. No fa falta llegir les dades per teclat, es pot inicialitzar al codi.

Mostra el contingut de tota la llista segons s’indica a l’exercici 3.

Mostra la quantitat d’individus majors d’edat.

Mostra la mitjana del pes de tots els individus.

Mostra els noms què s’han repetit o el missatge “SENSE NOMS REPETITS”.
"""

llistaPersones = [
    {"nom": "Pedro", "cognom": "Sanchez", "edat": 54, "pes": 67},
    {"nom": "Fernando", "cognom": "Alonso", "edat": 43, "pes": 78},
    {"nom": "Pedro", "cognom": "Sanchez", "edat": 54, "pes": 67},
    {"nom": "Benito", "cognom": "Sanchez", "edat": 15, "pes": 89}
]

quantitatMajor = 0
aux = 0
suma = 0
nomRepetit = []
nomVistos = []
for persona in llistaPersones:
    print(f"Aquestes són les dades: {persona['nom']} {persona['cognom']} {persona["edat"]} Anys {persona['pes']}KG")
    if(persona["edat"] >= 18):
        quantitatMajor += 1
        
    
    if(persona["nom"] in nomVistos):
        if(persona["nom"] not in nomRepetit):
            nomRepetit.append(persona["nom"])   
    
    else:
        nomVistos.append(persona["nom"])
        
        
    suma = persona["pes"]
    aux = aux + suma
    
mitjana = aux / len(llistaPersones)

if nomRepetit:
    print("Noms repetits: ",",".join(nomRepetit))
else:
    print("SENSE NOMS REPETITS")



print(quantitatMajor)
print(mitjana)

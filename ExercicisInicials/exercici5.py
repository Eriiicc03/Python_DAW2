""" 5-Mostra tots els individus de l’exercici 4, què són majors d’edat i tenen un pes igual o 
superior a la mitjana."""


llistaPersones = [
    {"nom": "Pedro", "cognom": "Sanchez", "edat": 54, "pes": 67},
    {"nom": "Fernando", "cognom": "Alonso", "edat": 43, "pes": 78},
    {"nom": "Pedro", "cognom": "Sanchez", "edat": 54, "pes": 67},
    {"nom": "Benito", "cognom": "Sanchez", "edat": 15, "pes": 89}
]

quantitatMajor = 0
aux = 0
suma = 0
pesSuperior = []
pesIgual = []
majorEdat = []
nomRepetit = []
nomVistos = []
for persona in llistaPersones:
    print(f"Aquestes són les dades: {persona['nom']} {persona['cognom']} {persona["edat"]} Anys {persona['pes']}KG")
    if(persona["edat"] >= 18):
        quantitatMajor += 1
        if(persona["nom"] in majorEdat):
            majorEdat.append(persona["nom"])
    
    if(persona["nom"] in nomVistos):
        if(persona["nom"] not in nomRepetit):
            nomRepetit.append(persona["nom"])   
        
    else:
        nomVistos.append(persona["nom"])
        
    suma = persona["pes"]
    aux = aux + suma
    
    mitjana = aux / len(llistaPersones)

    if(persona["pes"] >= mitjana and persona["edat"] >= 18):
        pesSuperior.append(persona["nom"])


if nomRepetit:
    print("Noms repetits: ",",".join(nomRepetit))
else:
    print("SENSE NOMS REPETITS")


print(pesSuperior)
print(quantitatMajor)
print(mitjana)

""" 
3-Crea un diccionari, amb diverses dades d’un individu, seguint aquesta estructura:

{“nom”: …. , “cognom”: …. , “edat”: …. , “pes”: …. }

Demana les dades per teclat i mostra la informació al final. Si l’individu és major d’edat, afegeix “(major d’edat)”.

Exemple 1:

Entra nom: Bob Esponja

Entra cognom: SquarePants

Entra edat: 15

Entra pes: 0.2

Aquestes són les dades: Bob Esponja SquarePants 15 anys 0.2 Kg

Exemple 2:

Entra nom: Arenita

Entra cognom: Mejillas

Entra edat: 19

Entra pes: 1.1

Aquestes són les dades: Arenita Mejillas 19 anys 1.1 Kg (major d’edat)"""

diccionari ={
    "nom": "",
    "cognom": "",
    "edat": 0,
    "pes": 0
}

diccionari["nom"] = input("Nom: ")
diccionari["cognom"] = input("Cognom: ")
diccionari["edat"] = int(input("Edat: "))
diccionari["pes"] = int(input("Pes: "))

texto = ""
if diccionari["edat"] >= 18:
    texto = "(Major d'edat)"
    
else:
    texto = "(menor d'edat)"
    
print(f"Aquestes són les dades: {diccionari['nom']} {diccionari['cognom']} {diccionari["edat"]} {diccionari['pes']} {texto}")
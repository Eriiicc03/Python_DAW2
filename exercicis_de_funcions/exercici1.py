"""
1- Crea una funció longituds que a partir d’una llista de paraules i una longitud, retorni tres valors: 
quantes paraules tenen la mateixa longitud, quantes una longitud inferior i quantes una longitud superior.
iguals, petites, grans = longituds(paraules, lon)
"""

def longituds (paraules, lon):
    iguals = 0
    petites = 0
    grans = 0
    
    for paraula in paraules:
        if len(paraula) == lon:
            iguals += 1
        elif len(paraula) < lon:
            petites += 1
        else:
            grans +=1
            
    return iguals, petites, grans

lon = int(input("Quina longitud ha de tenir la paraula? "))
paraules = ["casa", "sol", "ordinador", "gat", "taula"]

print(longituds(paraules, lon))  


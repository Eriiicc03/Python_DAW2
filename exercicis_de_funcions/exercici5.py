"""
5- Crea una funció temps que calculi la quantitat d’hores, minuts i segons d’un temps donat en segons.
hores, minuts, segons = temps(segons)
"""

def calcula_hores(hores,minuts,segons):
    total = segons / 3600 + minuts / 60 + hores
    
    return total


hores = int(input("Introdueix hores: "))
minuts = int(input("Introdueix minuts: "))
segons = int(input("Introdueix segons: "))

print(f"hores total: {calcula_hores(hores,minuts,segons)}")
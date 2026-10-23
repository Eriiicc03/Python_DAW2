"""4- Crea una funció calcula_segons que calculi la quantitat de segons en un temps donat en hores, 
minuts i segons. segons = calcula_segons( hores, minuts, segons)"""

def calcula_segons(hores,minuts,segons):
    total = hores * 3600 + minuts * 60 + segons
    
    return total


hores = int(input("Introdueix hores: "))
minuts = int(input("Introdueix minuts: "))
segons = int(input("Introdueix segons: "))

print(f"Segons total: {calcula_segons(hores,minuts,segons)}")
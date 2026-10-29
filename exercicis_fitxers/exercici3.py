"""
3- Crea un mètode afegir, que escrigui el contingut d'una llista en un fitxer. 
S'ha de fer append, el contingut original del fitxer no s'ha d'esborrar.
"""
import os
import exercici1
Llista = ["platano", "manzana", "nocilla"]

def afegir (Llista, fitxer):
    if os.path.isfile(fitxer):
        with open (fitxer, 'a', encoding='utf-8') as arxiu:
            for element in Llista:
                arxiu.write(element +'\n')
    
if __name__ == '__main__':
    afegir(Llista, 'fitxer3.txt')
    exercici1.mostra('fitxer3.txt')
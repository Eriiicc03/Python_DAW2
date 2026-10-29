"""
4- Crea un mètode escriuPos, que escrigui una frase en un fitxer, 
a una posició concreta. Si la posició és incorrecta, 
ha de mostrar un missatge informatiu.
"""
import os
def escriuPos(nomFitxer, frase, posicio):
    longitud = 0
    text = ""
    if os.path.isfile(nomFitxer):
        with open(nomFitxer, 'r', encoding='utf-8') as desti: 
            text = desti.read()
            longitud = len(text)
            if posicio < 0 or posicio > longitud:
                print("Posicio incorrecte")
            else:
                nouText = text[:posicio] + frase + text[posicio:]
                with open(nomFitxer, 'w', encoding='utf-8') as desti:
                    desti.write(nouText)
    else:
        print("El fitxer no existeix")

if __name__ == '__main__':
    escriuPos('fitxer4.txt', ' funcionaaa ', 2)
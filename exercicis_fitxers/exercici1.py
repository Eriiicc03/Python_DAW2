"""
1- Crea un mètode mostra, que a partir d'un nom de fitxer, mostri el seu contingut per consola. Si el fitxer no és vàlid, 
ha de mostrar un missatge informatiu.
"""
import os



def mostra(nomFitxer):
    if  os.path.isfile(nomFitxer):
        with open (nomFitxer, 'r',encoding='utf-8') as fitxer:
            for linia in fitxer: 
                print(linia)
    else:
        print("El nom del fitxer no es valid")
if __name__ == '__main__':
    mostra('fitxer.txt')
    mostra('novalid.txt')




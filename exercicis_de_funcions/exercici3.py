"""3- Crea una funció valorsRang que a partir d’una llista de valors, un valor mínim i un valor màxim, 
retorni una nova llista amb tots els valors de la primera què es troben entre els dos valors entrats 
per teclat (inclosos), sense valors repetits.
"""

def valorsRang(llista, valmin, valmax):
    llistaNova = []
    for i in llista:
        if i <= valmax and i >= valmin and i not in llistaNova:
            llistaNova.append(i)
    
    return llistaNova


valmin = int(input("Introdueix un valor minim: "))
valmax = int(input("Introdueix un valor maxim: "))
llista = [1,2,3,3,4,5,6,7,8,9]

print (f"Llista nova: ${valorsRang(llista,valmin, valmax)}")

#escollits=valorsRang(llista, valmin, valmax)
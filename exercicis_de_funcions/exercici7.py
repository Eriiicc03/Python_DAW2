"""
7-Crea una funció canviaMorse programa que sigui capaç de transformar text natural a codi morse i viceversa.
Heu de detectar automàticament de quin tipus es tracta i realitzar la conversió.
En morse se suporta ratlla "-", punt ".", s'ha de fer servir un espai " " per separar lletres i dos espais "  " entre paraules.
L'alfabet morse suportat serà el mostrat a https://es.wikipedia.org/wiki/Código_morse.

"""
lletres = "abcdefghijklmnñopqrstuvwxyz0123456789"
codisMorse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
              "-.-", ".-..", "--", "-.", "--.--", "---", ".--.", "--.-", ".-.", "...",
              "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
              "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]


def esMorse(text):
    for caracter in text:
        if caracter not in ".- ":
            return False
    return True


def canviaMorse(text):
    resultat = ""
    if esMorse(text):
        paraules = text.split("  ")
        for paraula in paraules:
            for codi in paraula.split(" "):
                if codi in codisMorse:
                    posicio = codisMorse.index(codi)
                    resultat = resultat + lletres[posicio]
            resultat = resultat + " "
    else:
        paraules = text.lower().split(" ")
        for paraula in paraules:
            for lletra in paraula:
                if lletra in lletres:
                    posicio = lletres.index(lletra)
                    resultat = resultat + codisMorse[posicio] + " "
            resultat = resultat + " "
    return resultat.strip()


text = input("Introdueix un text o codi morse:")
print(canviaMorse(text))
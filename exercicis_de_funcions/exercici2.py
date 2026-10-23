def puntsDaus (dau1, dau2):
    punts = dau1 + dau2
    puntsExtres = 0

    if dau1 < 3 or dau2 < 3:
        punts = 0
        return punts

    if punts > 12:
        puntsExtres = puntsExtres + 2

    if dau1 == 6:
        puntsExtres = puntsExtres + 1

    if dau2 == 6:
        puntsExtres = puntsExtres + 1

    punts = punts + puntsExtres
    return punts



dau1 = int(input("Dau 1: "))
dau2 = int(input("Dau 2: "))

print(f"Puntuacio: {puntsDaus(dau1, dau2)}")
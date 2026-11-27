import sqlite3
# -------------------------------------------------------------
# 8) El Torneig del Peix Daurat — 20 pt
#
# Després de travessar les Fosques Tombes del Nord, els aventurers
# arriben a una taverna on se celebra un peculiar torneig de pesca.
# Els participants utilitzen dos daus de sis cares (2d6) per pescar.
#
# Implementa un minijoc de pesca per torns amb un menú:
#   1. Mostrar rànquing
#   2. Pescar
#   3. Sortir
#
# Enunciat:
#   - Permet configurar el nombre de jugadors (mínim 2), els seus
#     noms i el nombre de rondes (entre 1 i 5).
#   - Cada jugador llança 2d6 i acumula punts segons el resultat:
#       * Daus diferents: suma el valor més alt i pot decidir
#         entre recollir els punts o continuar pescant.
#       * Daus iguals (excepte doble 6): pesca una bota, perd
#         els punts no guardats i finalitza el torn.
#       * Doble 6: pesca un peix llegendari, suma 12 punts
#         als acumulats, els guarda i finalitza el torn.
#   - Cada jugador participa una vegada per ronda.
#   - En acabar la partida, mostra la classificació final
#     ordenada per puntuació.
#   - Guarda les puntuacions al fitxer ranking_pesca.txt
#     (format: nom;punts), sense eliminar les anteriors.
#   - L'opció Mostrar rànquing ha de llegir el fitxer i mostrar
#     les 5 millors puntuacions històriques.
#   - El menú es repeteix fins que l'usuari selecciona Sortir.
#
# Proporciona les funcions:
#   tirar_daus(), calcular_pesca(dau1, dau2),
#   jugar_torn(nom_jugador), mostrar_classificacio(jugadors),
#   llegir_ranking(fitxer), guardar_puntuacions(jugadors, fitxer),
#   mostrar_ranking(), jugar_partida() i menu_pesca().
#
#   - Simula el llançament de dos daus de sis cares (2d6).
#     Pots utilitzar random.randint(1, 6) o qualsevol altra
#     solució que generi dos valors aleatoris entre 1 i 6.
#
#   - OPCIONAL: Pots reutilitzar la funció tirar("1d6", 1)
#     de l'exercici 7 per obtenir el valor de cada dau.
# -------------------------------------------------------------

import random
import sqlite3


def tirar_daus():
    """Simula dos daus de sis cares i retorna els resultats."""
    return random.randint(1, 6), random.randint(1, 6)


def calcular_pesca(dau1, dau2):
    """Retorna el tipus de pesca i els punts obtinguts."""
    if dau1 == 6 and dau2 == 6:
        return ('llegendari', 12)
    if dau1 == dau2:
        return ('bota', 0)
    return ('peix', max(dau1, dau2))


def jugar_torn(nom_jugador):
    """Gestiona un torn i retorna els punts guardats."""
    acumulats = 0
    print(f"\nTorn de {nom_jugador}")
    while True:
        dau1, dau2 = tirar_daus()
        tipus, punts = calcular_pesca(dau1, dau2)
        print(f"Daus: {dau1} i {dau2}")
        if tipus == 'bota':
            print("Has pescat una bota! Perds els punts d'aquest torn.")
            return 0
        acumulats += punts
        if tipus == 'llegendari':
            print(f"Peix llegendari! Guardes {acumulats} punts.")
            return acumulats
        print(f"Peix! +{punts} punts. Acumulats: {acumulats}")
        while True:
            opcio = input("Vols recollir els punts o continuar? (r/c): ").strip().lower()
            if opcio == 'r':
                print(f"Has guardat {acumulats} punts.")
                return acumulats
            if opcio == 'c':
                break
            print("ERROR: Escriu 'r' o 'c'.")


def mostrar_classificacio(jugadors):
    """Mostra la classificació de la partida, ordenada per punts."""
    ordenats = sorted(jugadors.items(), key=lambda element: element[1], reverse=True)
    print("\nCLASSIFICACIÓ DE LA PARTIDA\n")
    for posicio, (nom, punts) in enumerate(ordenats, 1):
        print(f"{posicio}. {nom:.<20} {punts} punts")
    if ordenats:
        print(f"\n    GUANYADOR: {ordenats[0][0].upper()}!")


def llegir_ranking(fitxer="ranking_pesca.txt"):
    """Llegeix les puntuacions històriques com a tuples (nom, punts)."""
    puntuacions = []
    try:
        with open(fitxer, 'r', encoding='utf-8') as arxiu:
            for linia in arxiu:
                parts = linia.strip().rsplit(';', 1)
                if len(parts) == 2:
                    try:
                        puntuacions.append((parts[0], int(parts[1])))
                    except ValueError:
                        pass
    except FileNotFoundError:
        pass
    return puntuacions


def mostrar_ranking():
    """Mostra les cinc millors puntuacions històriques."""
    print("\n====================================")
    print("    RÀNQUING DE PESCADORS")
    print("====================================\n")
    puntuacions = sorted(llegir_ranking(), key=lambda element: element[1], reverse=True)
    if not puntuacions:
        print("Encara no hi ha puntuacions registrades.\n")
        print("Sigues el primer a entrar\nal llibre dels grans pescadors!")
    else:
        for posicio, (nom, punts) in enumerate(puntuacions[:5], 1):
            print(f"{posicio}. {nom:.<20} {punts} punts")
    input("\nPrem INTRO per tornar al menú...")


def guardar_puntuacions(jugadors, fitxer="ranking_pesca.txt"):
    """Afegeix les puntuacions de la partida sense esborrar les antigues."""
    with open(fitxer, 'a', encoding='utf-8') as arxiu:
        for nom, punts in jugadors.items():
            arxiu.write(f"{nom};{punts}\n")


def jugar_partida():
    """Configura jugadors i rondes i gestiona el torneig."""
    print("\n====================================")
    print("    NOVA PARTIDA")
    print("====================================")
    while True:
        try:
            quantitat = int(input("Nombre de jugadors (mínim 2): "))
            if quantitat >= 2:
                break
        except ValueError:
            pass
        print("ERROR: Introdueix un nombre enter igual o superior a 2.")
    while True:
        try:
            rondes = int(input("Nombre de rondes (1-5): "))
            if 1 <= rondes <= 5:
                break
        except ValueError:
            pass
        print("ERROR: Introdueix un nombre enter entre 1 i 5.")

    jugadors = {}
    for i in range(1, quantitat + 1):
        while True:
            nom = input(f"Nom jugador {i}: ").strip()
            if nom and nom not in jugadors and ';' not in nom and '\n' not in nom:
                jugadors[nom] = 0
                break
            print("ERROR: El nom ha de ser vàlid i no pot estar repetit.")

    print("\nComença el torneig!")
    for ronda_actual in range(1, rondes + 1):
        print(f"\n========== RONDA {ronda_actual}/{rondes} ==========")
        for nom in jugadors:
            jugadors[nom] += jugar_torn(nom)
            print(f"Total de {nom}: {jugadors[nom]} punts")

    print("\n====================================")
    print("    FINAL DEL TORNEIG")
    print("====================================")
    mostrar_classificacio(jugadors)
    guardar_puntuacions(jugadors)
    print("\nLes puntuacions s'han guardat\nal llibre dels grans pescadors.")
    input("\nPrem INTRO per tornar al menú...")


def menu_pesca():
    """Mostra el menú fins que l'usuari decideixi sortir."""
    while True:
        print("\n====================================")
        print("   EL TORNEIG DEL PEIX DAURAT")
        print("====================================")
        print("1. Mostrar rànquing")
        print("2. Pescar")
        print("3. Sortir")
        opcio = input("\nEscull una opció: ").strip()
        if opcio == '1':
            mostrar_ranking()
        elif opcio == '2':
            jugar_partida()
        elif opcio == '3':
            print("\n====================================")
            print("Gràcies per visitar El Peix Daurat!\n")
            print("Que els daus t'acompanyin!")
            print("====================================")
            break
        else:
            print("\nERROR: Opció no vàlida.\nSelecciona una opció entre 1 i 3.")
            input("\nPrem INTRO per continuar...")

'''

OPCIO MOSTRAR RANKING. TEXT QUE HA DE MOSTRAR

====================================
    RÀNQUING DE PESCADORS
====================================

1. Arwen .............. 85 punts
2. Legolas ............ 74 punts
3. Elara .............. 67 punts
4. Thorin ............. 58 punts
5. Thorin ............. 52 punts

Prem INTRO per tornar al menú...

SINO HI HA DADES EN EL FITXER RANKING_PESCA.TXT

Encara no hi ha puntuacions registrades.

Sigues el primer a entrar
al llibre dels grans pescadors!

OPCIO NOVA PARTIDA. TEXT QUE HA DE MOSTRAR.

====================================
    NOVA PARTIDA
====================================

Nombre de jugadors (mínim 2): 3
Nombre de rondes (1-5): 4

Nom jugador 1: Thorin
Nom jugador 2: Elora
Nom jugador 3: Gandalf

Comença el torneig!

TEXT QUE HA DE SORTIR AL FINALITZAR LA PARTIDA.
====================================
    FINAL DEL TORNEIG
====================================

CLASSIFICACIÓ DE LA PARTIDA

1. Gandalf ............ 74 punts
2. Thorin ............. 58 punts
3. Elora .............. 34 punts

    GUANYADOR: GANDALF!

Les puntuacions s'han guardat
al llibre dels grans pescadors.



OPCIO SORTIR. TEXT QUE HA DE MOSTRAR.
====================================
Gràcies per visitar El Peix Daurat!

Que els daus t'acompanyin!
====================================

OPCIONS INCORRECTES.
Escull una opció: 8

ERROR: Opció no vàlida.

Selecciona una opció entre 1 i 3.

Prem INTRO per continuar...

'''


# -------------------------------------------------------------
# 9) El Bestiari Perdut  — 25 pt
#
# Un arxiu de monstres antics espera ser reconstruït.
# Implementa bestiari() que gestioni una base de dades SQLite (bestiari.db) amb:
# (id INTEGER PK, nom TEXT, cr INTEGER, hp INTEGER, tipus TEXT)
# Permet: afegir, buscar, llistar i eliminar monstres.
# Enunciat:
#   - Crea la taula si no existeix: monstres(id INTEGER PK, nom TEXT, cr INTEGER, hp INTEGER, tipus TEXT)
#   - Proporciona funcions: inicialitzar_bestiari(conn), add_monstre(dbpath, nom, cr, hp, tipus),
#     search_monstre(dbpath, term), list_monstres(dbpath), delete_monstre(dbpath, id)
def inicialitzar_bestiari(conn):
    """Crea la taula 'monstres' si no existeix (utilitzat pel test runner)."""
    # TODO: Implementa inicialitzar_bestiari(conn)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS monstres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            cr INTEGER,
            hp INTEGER,
            tipus TEXT
        )
    """)
    conn.commit()
    return
    raise NotImplementedError("Implementa inicialitzar_bestiari(conn)")

def pausa_bestiari():
    """Espera fins que l'usuari premi INTRO."""
    input("\nPrem INTRO per tornar al menú...")


def demanar_enter_positiu(missatge, camp):
    """Demana un enter no negatiu i repeteix si és incorrecte."""
    while True:
        try:
            valor = int(input(missatge))
            if valor >= 0:
                return valor
        except ValueError:
            pass
        print(f"ERROR: El {camp} ha de ser un nombre enter positiu.")


def mostrar_fila_monstre(monstre):
    """Mostra una criatura amb columnes alineades."""
    mid, nom, cr, hp, tipus = monstre
    print(f"{mid:<4} {nom:<20} {cr:<6} {hp:<6} {tipus}")


def add_monstre_p(db="bestiari.db"):
    print("\n==================================================")
    print("             REGISTRAR UNA CRIATURA")
    print("==================================================")
    print("\nL'arxiver prepara una nova pàgina del bestiari.\n")
    while True:
        nom = input("Nom del monstre: ").strip()
        if nom:
            break
        print("ERROR: El nom no pot estar buit.")
    cr = demanar_enter_positiu("Nivell de desafiament (CR): ", "CR")
    hp = demanar_enter_positiu("Punts de vida (HP): ", "HP")
    while True:
        tipus = input("Tipus de criatura: ").strip()
        if tipus:
            break
        print("ERROR: El tipus no pot estar buit.")
    add_monstre(db, nom, cr, hp, tipus)
    print("\n--------------------------------------------------")
    print("El monstre s'ha registrat correctament!\n")
    print(f"Nom: {nom}\nCR: {cr}\nHP: {hp}\nTipus: {tipus}")
    print("--------------------------------------------------")
    pausa_bestiari()


def add_monstre(dbpath: str, nom: str, cr: int, hp: int, tipus: str) -> int:
    """Afegeix un monstre i retorna l'identificador generat."""
    with sqlite3.connect(dbpath) as conn:
        inicialitzar_bestiari(conn)
        cur = conn.execute("INSERT INTO monstres (nom, cr, hp, tipus) VALUES (?, ?, ?, ?)",
                           (nom, cr, hp, tipus))
        return cur.lastrowid


def search_monstre_p(db="bestiari.db"):
    print("\n==================================================")
    print("              CERCAR UNA CRIATURA")
    print("==================================================")
    print("\nL'arxiver consulta les pàgines del bestiari...\n")
    term = input("Introdueix el nom o part del nom: ")
    cerca = search_monstre(db, term)
    print("\n--------------------------------------------------")
    if not cerca:
        print("No s'ha trobat cap criatura amb aquest nom.")
    else:
        print("RESULTATS DE LA CERCA")
        print("--------------------------------------------------")
        print("ID   NOM                  CR     HP     TIPUS")
        print("--------------------------------------------------")
        for monstre in cerca:
            mostrar_fila_monstre(monstre)
        print("--------------------------------------------------")
        print(f"\nS'han trobat {len(cerca)} criatures.")
    pausa_bestiari()


def search_monstre(dbpath: str, term: str):
    """Cerca coincidències parcials del nom i retorna tuples."""
    with sqlite3.connect(dbpath) as conn:
        inicialitzar_bestiari(conn)
        return conn.execute("SELECT * FROM monstres WHERE nom LIKE ? ORDER BY id",
                            (f"%{term}%",)).fetchall()


def list_monstres_p(db="bestiari.db"):
    print("\n==================================================")
    print("           CRIATURES DEL BESTIARI")
    print("==================================================")
    llistat = list_monstres(db)
    if not llistat:
        print("\nEl gran llibre encara no conté cap criatura.\n")
        print("El bestiari està buit.")
    else:
        print("\nL'arxiver desplega les pàgines del gran llibre...\n")
        print("ID   NOM                  CR     HP     TIPUS")
        print("--------------------------------------------------")
        for monstre in llistat:
            mostrar_fila_monstre(monstre)
        print("--------------------------------------------------")
        print(f"\nTotal de criatures registrades: {len(llistat)}")
    pausa_bestiari()


def list_monstres(dbpath: str):
    """Retorna totes les criatures com a tuples."""
    with sqlite3.connect(dbpath) as conn:
        inicialitzar_bestiari(conn)
        return conn.execute("SELECT * FROM monstres ORDER BY id").fetchall()


def delete_monstre_p(db="bestiari.db"):
    print("\n==================================================")
    print("              ELIMINAR UNA CRIATURA")
    print("==================================================")
    print('\nL\'arxiver adverteix:')
    print('"Una criatura esborrada desapareixerà del llibre."\n')
    mid = demanar_enter_positiu("Introdueix l'ID del monstre: ", "ID")
    with sqlite3.connect(db) as conn:
        inicialitzar_bestiari(conn)
        monstre = conn.execute("SELECT * FROM monstres WHERE id = ?", (mid,)).fetchone()
    print("\n--------------------------------------------------")
    if monstre is None:
        print(f"\nERROR: No existeix cap criatura amb l'ID {mid}.")
        print("\nNo s'ha eliminat cap registre.")
        pausa_bestiari()
        return
    _, nom, cr, hp, tipus = monstre
    print("CRIATURA SELECCIONADA")
    print("--------------------------------------------------")
    print(f"ID: {mid}\nNom: {nom}\nCR: {cr}\nHP: {hp}\nTipus: {tipus}")
    print("--------------------------------------------------")
    while True:
        resposta = input("\nSegur que vols eliminar aquesta criatura? (s/n): ").strip().lower()
        if resposta in ('s', 'n'):
            break
        print("ERROR: Respon 's' o 'n'.")
    if resposta == 's':
        eliminats = delete_monstre(db, mid)
        if eliminats:
            print(f"\nEl monstre {nom} s'ha eliminat correctament\ndel bestiari.")
        else:
            print("\nNo s'ha eliminat cap registre.")
    else:
        print("\nOperació cancel·lada.\n\nLa criatura continua registrada al bestiari.")
    pausa_bestiari()


def delete_monstre(dbpath: str, mid: int) -> int:
    """Elimina per identificador i retorna el nombre de files afectades."""
    with sqlite3.connect(dbpath) as conn:
        inicialitzar_bestiari(conn)
        cur = conn.execute("DELETE FROM monstres WHERE id = ?", (mid,))
        return cur.rowcount


def menu_bestiari(db="bestiari.db"):
    """Gestiona el menú interactiu del bestiari."""
    with sqlite3.connect(db) as conn:
        inicialitzar_bestiari(conn)
    while True:
        print("\n========================================")
        print("       BESTIARI DE LES FOSQUES TOMBES")
        print("========================================")
        print("1. Afegir un monstre")
        print("2. Cercar un monstre")
        print("3. Mostrar tots els monstres")
        print("4. Eliminar un monstre")
        print("5. Sortir")
        opcio = input("\nEscull una opció: ").strip()
        if opcio == '1':
            add_monstre_p(db)
        elif opcio == '2':
            search_monstre_p(db)
        elif opcio == '3':
            list_monstres_p(db)
        elif opcio == '4':
            delete_monstre_p(db)
        elif opcio == '5':
            print("\n==================================================")
            print("          BESTIARI DE LES FOSQUES TOMBES")
            print("==================================================")
            print("\nL'arxiver tanca lentament el gran llibre.\n")
            print('"El coneixement de les criatures és una arma')
            print('tan poderosa com qualsevol espasa."')
            print("\nFins a la pròxima aventura!")
            print("==================================================")
            break
        else:
            print("\nERROR: Opció no vàlida.\nSelecciona una opció entre 1 i 5.")
            input("\nPrem INTRO per continuar...")

'''
OPCIO AFEGIR MONSTRE. TEXT QUE HA DE MOSTRAR
==================================================
             REGISTRAR UNA CRIATURA
==================================================

L'arxiver prepara una nova pàgina del bestiari.

Nom del monstre: Goblin
Nivell de desafiament (CR): 1
Punts de vida (HP): 7
Tipus de criatura: Humanoide

--------------------------------------------------

El monstre s'ha registrat correctament!

Nom: Goblin
CR: 1
HP: 7
Tipus: Humanoide

--------------------------------------------------
Prem INTRO per tornar al menú...

SI FIQUEN ALGUN VALOR INCORRECTE, EL PROGRAMA HA DE TORNAR A DEMANAR EL VALOR

Nivell de desafiament (CR): -3

ERROR: El CR ha de ser un nombre enter positiu.

Nivell de desafiament (CR):



OPCIO CERCAR MONSTRE. TEXT QUE HA DE MOSTRAR. 

==================================================
              CERCAR UNA CRIATURA
==================================================

L'arxiver consulta les pàgines del bestiari...

Introdueix el nom o part del nom: Gob

--------------------------------------------------
RESULTATS DE LA CERCA
--------------------------------------------------

ID   NOM                 CR     HP     TIPUS
--------------------------------------------------
1    Goblin              1      7     Humanoide
5    Goblin Capità       3     35     Humanoide
8    Goblin Xaman        2     18     Humanoide

--------------------------------------------------

S'han trobat 3 criatures.

Prem INTRO per tornar al menú...

SI NO ES TROBA CAP

==================================================
              CERCAR UNA CRIATURA
==================================================

Introdueix el nom o part del nom: Drac Blau

--------------------------------------------------

No s'ha trobat cap criatura amb aquest nom.

Prem INTRO per tornar al menú...


OPCIO LLISTAT MONSTRES. TEXT QUE HA DE MOSTRAR.
==================================================
           CRIATURES DEL BESTIARI
==================================================

L'arxiver desplega les pàgines del gran llibre...

ID   NOM                 CR     HP     TIPUS
--------------------------------------------------
1    Goblin               1      7    Humanoide
2    Esquelet             1     13    No-mort
3    Orc                  2     15    Humanoide
4    Troll                5     84    Gegant
5    Goblin Capità        3     35    Humanoide
6    Drac Vermell        15    256    Drac

--------------------------------------------------

Total de criatures registrades: 6

Prem INTRO per tornar al menú...

SI EL BESTIARI ESTÀ BUIT.

==================================================
           CRIATURES DEL BESTIARI
==================================================

El gran llibre encara no conté cap criatura.

El bestiari està buit.

Prem INTRO per tornar al menú...


OPCIO ELIMINAR MONSTRE. TEXT QUE HA DE MOSTRAR
==================================================
             ELIMINAR UNA CRIATURA
==================================================

L'arxiver adverteix:
"Una criatura esborrada desapareixerà del llibre."

Introdueix l'ID del monstre: 4

--------------------------------------------------
CRIATURA SELECCIONADA
--------------------------------------------------

ID: 4
Nom: Troll
CR: 5
HP: 84
Tipus: Gegant

--------------------------------------------------

Segur que vols eliminar aquesta criatura? (s/n): s

--------------------------------------------------

El monstre Troll s'ha eliminat correctament
del bestiari.

Prem INTRO per tornar al menú...

SI L'USUARI CANCEL·LA

Segur que vols eliminar aquesta criatura? (s/n): n

Operació cancel·lada.

La criatura continua registrada al bestiari.

Prem INTRO per tornar al menú...

SI L'IDENTIFICADOR NO EXISTEIX.
Introdueix l'ID del monstre: 99

--------------------------------------------------

ERROR: No existeix cap criatura amb l'ID 99.

No s'ha eliminat cap registre.

Prem INTRO per tornar al menú...


OPCIO SORTIR. TEXT QUE HA DE MOSTRAR.
==================================================
          BESTIARI DE LES FOSQUES TOMBES
==================================================

L'arxiver tanca lentament el gran llibre.

"El coneixement de les criatures és una arma
tan poderosa com qualsevol espasa."

Fins a la pròxima aventura!

==================================================


OPCIONS INCORRECTES.
Escull una opció: 8

ERROR: Opció no vàlida.

Selecciona una opció entre 1 i 5.

Prem INTRO per continuar...
'''


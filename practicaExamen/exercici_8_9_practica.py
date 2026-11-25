
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


# TODO: importa els mòduls que necessitis


def tirar_daus():
    """Simula dos daus de sis cares i retorna els resultats (dau1, dau2)."""
    # TODO
    pass


def calcular_pesca(dau1, dau2):
    """Retorna una tupla (tipus, punts).
    tipus pot ser 'peix', 'bota' o 'llegendari'."""
    # TODO
    pass


def jugar_torn(nom_jugador):
    """Gestiona el torn d'un jugador i retorna els punts guardats.
    - Peix: suma el dau més alt i pregunta si recollir (r) o continuar (c).
    - Bota: perd els punts del torn i acaba.
    - Doble 6: suma 12, guarda i acaba."""
    # TODO
    pass


def mostrar_classificacio(jugadors):
    """Mostra la classificació de la partida ordenada per punts
    i el nom del guanyador."""
    # TODO
    pass


def llegir_ranking(fitxer="ranking_pesca.txt"):
    """Llegeix el fitxer (format nom;punts) i retorna una llista
    de tuples (nom, punts). Si el fitxer no existeix, retorna []."""
    # TODO
    pass


def guardar_puntuacions(jugadors, fitxer="ranking_pesca.txt"):
    """Afegeix les puntuacions al fitxer SENSE esborrar les anteriors."""
    # TODO
    pass


def mostrar_ranking():
    """Mostra les 5 millors puntuacions històriques."""
    # TODO
    pass


def jugar_partida():
    """Demana jugadors (mínim 2), noms i rondes (1-5),
    juga el torneig, mostra la classificació i guarda les puntuacions."""
    numJugadors = int(input("Nombre de jugadors (mínim 2): "))
    jugadors = []
    for i in range(numJugadors):
        nom = input(f"Nom jugador {i+1}: ")
        jugadors.append((nom, 0))
    
    numRondes = int(input("Nombre de rondes (1-5): "))
    for ronda in range(numRondes):
        print(f"\nRonda {ronda + 1} de {numRondes}")
        for i in range(numJugadors):
            nom, _ = jugadors[i]
            punts = jugar_torn(nom)
            jugadors[i] = (nom, punts)
        


def menu_pesca():
    """Mostra el menú (1. Rànquing, 2. Pescar, 3. Sortir)
    fins que l'usuari esculli Sortir."""
    match input("escull una opció:\n 1. Mostrar rànquing\n 2. Pescar\n 3. Sortir\n "):
        case "1":
            mostrar_ranking()
        case "2":
            jugar_partida()
        case "3":
            pass

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
    """Crea la taula 'monstres' si no existeix."""
    # TODO
    pass


def add_monstre(dbpath: str, nom: str, cr: int, hp: int, tipus: str) -> int:
    """Afegeix un monstre i retorna l'id generat."""
    # TODO (substitueix aquest return pel teu codi)
    return 0


def search_monstre(dbpath: str, term: str):
    """Cerca monstres que continguin 'term' al nom.
    Retorna una llista de tuples (id, nom, cr, hp, tipus)."""
    # TODO
    pass


def list_monstres(dbpath: str):
    """Retorna tots els monstres com a llista de tuples."""
    # TODO
    pass


def delete_monstre(dbpath: str, mid: int) -> int:
    """Elimina el monstre amb aquest id.
    Retorna el nombre de files eliminades (0 o 1)."""
    # TODO (substitueix aquest return pel teu codi)
    return 0


def bestiari(db="bestiari.db"):
    """Menú interactiu:
    1. Afegir  2. Cercar  3. Mostrar tots  4. Eliminar  5. Sortir
    Valida que CR, HP i ID siguin enters positius i que nom/tipus no siguin buits.
    Pots crear les funcions auxiliars que necessitis."""
    # TODO
    pass

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


if __name__ == "__main__":
    menu_pesca()
    # bestiari()

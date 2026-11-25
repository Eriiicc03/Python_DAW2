"""Gestion de una agenda
"""
DB = 'agenda.db'

import sqlite3
def inicializar_agenda(conn):
    """Crea la tabla 'contactos' si no existe.

    Args:
        conn (sqlite3.Connection): Conexión abierta a la base de datos.
    """
    conn = sqlite3.connect(DB)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT,
            email TEXT UNIQUE
        )
    """)
    conn.commit()

def add_contacto(dbpath, nombre, telefono, email):
    """Añadimos un contacto

    Args:
        dbpath (str): Ruta fichero.
        nombre (str): Nombre del contacto.
        telefono (str): telefono de contacto.
        email (str): Emaiil (no se puede repetir).

    Returns:
        int: Id generado para el contacto
        
    Raises:
        sqlite3.IntegrityError: Si el email ya existe
    """
    with sqlite3.connect(dbpath) as conn:
        inicializar_agenda(conn)
        cur = conn.execute("INSERT INTO contactos (nombre, telefono, email)" "VALUES (?, ?, ?)", (nombre, telefono, email))
    return cur.lastrowid

def search_contacto(dbpath, termino):
    with sqlite3.connect(dbpath) as conn:
        inicializar_agenda(conn)
        cur = conn.execute(
            "SELECT * FROM contactos WHERE nombre LIKE ? ORDER BY id",
            (f"%{termino}%",)
        )    
    return cur.fetchall()
    
if __name__ == "__main__":
    
    #inicializar_agenda(conn=DB)
    #add_contacto(DB, "eric", "640856007", "eric@gmail.com")
    search_contacto(DB, "eric")
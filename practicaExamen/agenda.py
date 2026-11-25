"""Agenda de contactos guardada en una base de datos SQLite."""
import sqlite3
DB = 'agenda.db'


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
    """Inserta un contacto nuevo en la agenda.

    Args:
        dbpath (str): Ruta de la base de datos.
        nombre (str): Nombre del contacto.
        telefono (str): Teléfono del contacto.
        email (str): Email del contacto (no se puede repetir).

    Returns:
        int: Id generado para el contacto.

    Raises:
        sqlite3.IntegrityError: Si el email ya existe.
    """
    with sqlite3.connect(dbpath) as conn:
        inicializar_agenda(conn)
        cur = conn.execute(
            "INSERT INTO contactos (nombre, telefono, email)"
            "VALUES (?, ?, ?)",
            (nombre, telefono, email))
    return cur.lastrowid


def search_contacto(dbpath, termino):
    """Busca contactos cuyo nombre contenga el término.

    Args:
        dbpath (str): Ruta de la base de datos.
        termino (str): Texto a buscar dentro del nombre.

    Returns:
        list[tuple]: Filas (id, nombre, telefono, email) ordenadas por id.
        Lista vacía si no hay coincidencias.
    """
    with sqlite3.connect(dbpath) as conn:
        inicializar_agenda(conn)
        cur = conn.execute(
            "SELECT * FROM contactos WHERE nombre LIKE ? ORDER BY id",
            (f"%{termino}%",)
        )
    return cur.fetchall()


def list_contactos(dbpath):
    """Obtiene todos los contactos ordenados por nombre.

    Args:
        dbpath (str): Ruta de la base de datos.

    Returns:
        list[tuple]: Filas (id, nombre, telefono, email).
    """
    with sqlite3.connect(dbpath) as conn:
        inicializar_agenda(conn)
        cur = conn.execute("SELECT * FROM contactos ORDER BY nombre")
    return cur.fetchall()


def update_telefono(dbpath, id_contacto, telefono):
    """Cambia el teléfono de un contacto.

    Args:
        dbpath (str): Ruta de la base de datos.
        id_contacto (int): Id del contacto a modificar.
        telefono (str): Nuevo teléfono.

    Returns:
        int: Filas modificadas (1 si el contacto existe, 0 si no).
    """
    with sqlite3.connect(dbpath) as conn:
        inicializar_agenda(conn)
        cur = conn.execute(
            "UPDATE contactos set telefono = ? WHERE id = ?",
            (telefono, id_contacto)
        )
        return cur.rowcount


def delete_contacto(dbpath, id_contacto):
    """Elimina un contacto por su id.

    Args:
        dbpath (str): Ruta de la base de datos.
        id_contacto (int): Id del contacto a eliminar.

    Returns:
        int: Filas eliminadas (1 si el contacto existía, 0 si no).
    """
    with sqlite3.connect(dbpath) as conn:
        inicializar_agenda(conn)
        cur = conn.execute(
            "DELETE FROM contactos WHERE id = ?",
            (id_contacto,)
        )
        return cur.rowcount


def menu_agenda(db=DB):
    """Muestra el menú de la agenda hasta que el usuario elige salir.

    Args:
        db (str): Ruta de la base de datos.
    """
    while True:
        print("\n1. Añadir\n2. Buscar\n3. Listar\n4. Eliminar\n5. Salir")
        opcion = input("Opción: ").strip()
        match opcion:
            case "1":
                nombre = input("Nombre: ").strip()
                telefono = input("Teléfono: ").strip()
                email = input("Email: ").strip()
                try:
                    nuevo_id = add_contacto(db, nombre, telefono, email)
                except sqlite3.IntegrityError:
                    print("ERROR: Ese email ya está registrado.")
                else:
                    print(f"Contacto guardado con id {nuevo_id}.")
            case "2":
                resultados = search_contacto(db, input("Buscar: ").strip())
                for id_, nombre, telefono, email in resultados:
                    print(f"{id_:<4} {nombre:<20} {telefono:<12} {email}")
                if not resultados:
                    print("No hay ningún contacto con ese nombre.")
            case "3":
                for id_, nombre, telefono, email in list_contactos(db):
                    print(f"{id_:<4} {nombre:<20} {telefono:<12} {email}")
            case "4":
                try:
                    id_contacto = int(input("Id: "))
                except ValueError:
                    print("ERROR: El id debe ser un número.")
                    continue
                if delete_contacto(db, id_contacto):
                    print("Contacto eliminado.")
                else:
                    print("No existe ningún contacto con ese id.")
            case "5":
                break
            case _:
                print("ERROR: Opción no válida.")


if __name__ == "__main__":
    menu_agenda()

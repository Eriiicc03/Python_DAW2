import sqlite3
DB = './biblioteca.db'

def inicializar_biblioteca(conn):
    conn = sqlite3.connect(DB)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            isbn TEXT UNIQUE NOT NULL,
            titulo TEXT NOT NULL, 
            autor TEXT, 
            anio INTEGER,
            disponible INTEGER DEFAULT 1
        )
    """)
    conn.commit()
    
def add_libro(dbpath, isbn, titulo, autor, anio):
    with sqlite3.connect(dbpath) as conn:
        inicializar_biblioteca(conn)
        cur = conn.execute(
            "INSERT INTO libros (isbn, titulo, autor, anio)"
            "VALUES (?, ?, ?, ?)",
            (isbn, titulo, autor, anio))
    return cur.lastrowid

def buscar_por_autor(dbpath, autor):
    with sqlite3.connect(dbpath) as conn:
        inicializar_biblioteca(conn)
        cur = conn.execute(
            "SELECT * FROM libros WHERE autor LIKE ?",
            (f"%{autor}%",)
        )
    
    return cur.fetchall()
    
def listar_disponibles(dbpath):
    with sqlite3.connect(dbpath) as conn: 
        inicializar_biblioteca(conn)
        cur = conn.execute(
            "SELECT * FROM libros WHERE disponible = 1"
        )
    return cur.fetchall()

def prestar_libro(dbpath, id_libro):
    with sqlite3.connect(dbpath) as conn:
        inicializar_biblioteca(conn)
        cur = conn.execute(
            "UPDATE libros SET disponible = 0 WHERE id = ? AND disponible = 1",
            (id_libro,)
        )
        return cur.rowcount
    
def devolver_libro(dbpath, id_libro):
    with sqlite3.connect(dbpath) as conn:
        inicializar_biblioteca(conn)
        cur = conn.execute(
            "UPDATE libros SET disponible = 1 WHERE id = ? AND disponible = 0",
            (id_libro,)
        )
        return cur.rowcount

def delete_libro(dbpath, id_libro):
    with sqlite3.connect(dbpath) as conn: 
        inicializar_biblioteca(conn)
        cur = conn.execute(
            "DELETE FROM libros WHERE id = ?",
            (id_libro,)
        )
        return cur.rowcount
if __name__ == "__main__":
    inicializar_biblioteca(DB)
    #add_libro(dbpath=DB, isbn='1', titulo='prueba', autor='Eric',anio=2020)
    print(buscar_por_autor(dbpath=DB, autor='Eric'))
    prestar_libro(dbpath=DB, id_libro=1)
    print(listar_disponibles(dbpath=DB))
    devolver_libro(dbpath=DB, id_libro=1)
    print(listar_disponibles(dbpath=DB))
    delete_libro(dbpath=DB, id_libro=1)
    print(listar_disponibles(dbpath=DB))

    
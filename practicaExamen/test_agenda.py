"""Tests del módulo agenda."""

import sqlite3

import pytest

from agenda import (add_contacto, delete_contacto, list_contactos,
                    search_contacto, update_telefono)


@pytest.fixture
def db(tmp_path):
    """Base de datos temporal con dos contactos."""
    ruta = tmp_path / "test.db"
    add_contacto(ruta, "Ana López", "600111222", "ana@mail.com")
    add_contacto(ruta, "Bruno Díaz", "600333444", "bruno@mail.com")
    return ruta


def test_add_en_bd_vacia_devuelve_id_1(tmp_path):
    assert add_contacto(tmp_path / "vacia.db", "Eva", "1", "eva@mail.com") == 1


def test_email_repetido_lanza_error(db):
    with pytest.raises(sqlite3.IntegrityError):
        add_contacto(db, "Otra Ana", "999", "ana@mail.com")


def test_buscar_ana(db):
    resultado = search_contacto(db, "Ana")
    assert len(resultado) == 1
    assert resultado[0][1] == "Ana López"


def test_update_telefono(db):
    assert update_telefono(db, 1, "699000000") == 1
    assert search_contacto(db, "Ana")[0][2] == "699000000"


def test_borrar_id_inexistente(db):
    assert delete_contacto(db, 99) == 0
    assert len(list_contactos(db)) == 2

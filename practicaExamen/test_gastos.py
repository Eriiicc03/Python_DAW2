import pytest
from gastos import guardar_gasto, leer_gastos, top_gastos, total_gastos
FICHERO_GASTOS = "gastos.txt"
def test_leer_gastos(tmp_path):
    assert leer_gastos(tmp_path / "no_existe.txt") == []

def test_guardar_gasto(tmp_path):
    fichero = tmp_path / "gastos.txt"
    guardar_gasto(fichero,"Cine",8.5)
    guardar_gasto(fichero,"Gasolina",40)
    assert leer_gastos(fichero) == [("Cine",8.5), ("Gasolina",40)]

def test_fichero_basura(tmp_path):
    fichero = tmp_path / "basura.txt"
    fichero.write_text("Pan;1.2\nbasura\nLeche;abc\n", encoding="utf-8")
    assert leer_gastos(fichero) == [("Pan", 1.2)]

def test_total_gastos(tmp_path):
    assert total_gastos([("a", 0.1),("b", 0.2)]) == pytest.approx(0.3)


def test_top_gastos():
    gastos = [("a", 5), ("b", 50), ("c", 20), ("d", 1)]
    assert top_gastos(gastos, 2) == [("b", 50), ("c", 20)]


def test_importe_negativo_lanza_error(tmp_path):
    fichero = tmp_path / "gastos.txt"
    with pytest.raises(ValueError):
        guardar_gasto(fichero, "Cine", -3)
    assert leer_gastos(fichero) == []

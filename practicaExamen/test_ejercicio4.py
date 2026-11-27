import pytest
from ejercicio4 import media, calificacion
class TestMedia:
    def test_media_enteros(self):
        assert media([4, 6, 8]) == 6

    def test_media_decimales(self):
        assert media([5, 7, 3.6]) == pytest.approx(5.2)

    def test_media_vacia(self):
        with pytest.raises(ValueError):
            media([])

class TestClasificacion:
    def test_fuera_de_rango(self):
        with pytest.raises(ValueError):
            calificacion(11)
        with pytest.raises(ValueError):
            calificacion(-1)
    
    def test_clasificacion_supenso(self):
        assert calificacion(3) == 'Suspenso'
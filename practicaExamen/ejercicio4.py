"""Calculo de la media de un alumno.
"""

def media(notas):
    """Calculo de la media del alumno.

    Args:
        notas (float): Media del alumno.

    Raises:
        ValueError: En caso de que no haya notas.

    Returns:
        float: Devuelve la nota media del alumno.
    """
    if not notas:
        raise ValueError("No hay notas")
    return sum(notas) / len(notas)


def calificacion(nota):
    """Clasifica las notas del alumno según unas condiciones.

    Args:
        nota (float): Nota del alumno.

    Raises:
        ValueError: En caso de que la nota sea incorrecta.

    Returns:
        Str: Retona un string segun la nota.
    """
    if nota < 0 or nota > 10:
        raise ValueError("Nota fuera de rango")
    if nota < 5:
        return "Suspenso"
    if nota < 7:
        return "Aprobado"
    if nota < 9:
        return "Notable"
    return "Excelente"


class Alumno:
    """Clase alumno
    """
    def __init__(self, nombre):
        """Objecto alumno.

        Args:
            nombre (str): Nombre del alumno.
        """
        self.nombre = nombre
        self.notas = []

    def poner_nota(self, nota):
        """Añadimos la nota a la lista.

        Args:
            nota (float): Nota del alumno.
        """
        calificacion(nota)
        self.notas.append(nota)

    def nota_final(self):
        """Retorno de la nota final.

        Returns:
            float: Devuelve la nota final.
        """
        return media(self.notas)
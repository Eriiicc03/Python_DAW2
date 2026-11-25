"""Gestión de gastos personales guardados en un fichero de texto.

Cada línea del fichero tiene el formato concepto;importe.
"""


FICHERO_GASTOS = "gastos.txt"


def guardar_gasto(fichero, concepto, importe):
    """Añade un gasto en el fichero.

    Args:
        fichero (str): Ruta del fichero
        concepto (str): Descripcion del gasto
        importe (float): Gasto

    Raises:
        ValueError: Si el concepto esta vacio o contiene ;
        ValueError: Si el importe es negativo
    """
    if not concepto or ";" in concepto:
        raise ValueError("El concepto no puede estar vacío ni contener ';'")
    if (importe < 0):
        raise ValueError("El importe no puede ser negativo")
    with open(fichero, 'a', encoding='utf-8') as f:
        f.write(f"{concepto};{importe}\n")


def leer_gastos(fichero):
    """Lee los gastos del fichero.

    Args:
        fichero (str): fichero donde esta los gastos guardados

    Returns:
        list (str, float): Devuelve una lista de tuplas con las partes de cada linea.
    """
    gastos = []
    try:
        with open(fichero, 'r', encoding='utf-8') as f:
            for linea in f:
                partes = linea.strip().split(";")
                if (len(partes) != 2):
                    continue
                try:
                    gastos.append((partes[0], float(partes[1])))
                except ValueError:
                    continue
    except FileNotFoundError:
        return []
    return gastos


def total_gastos(gastos):
    """Calcula el total de los gastos.

    Args:
        gastos (float): Suma del total de los calculos.

    Returns:
        float: Suma del total redondeada a 2 decimales.
    """
    total = sum(importe for _, importe in gastos)
    return round(total, 2)


def top_gastos(gastos, n=3):
    """Ordena por los gastos mas grandes.

    Args:
        gastos (list[tuple[str, float]]): Posicion de los gastos
        n (int, optional): Obtenemos los 3 gastos mas grande. Defaults to 3.

    Returns:
       list[tuple[str, float]]: Listas de los gastos mas caros
    """
    top = sorted(gastos, key=lambda gasto: gasto[1], reverse=True)
    return top[:n]


def menu_gastos(fichero=FICHERO_GASTOS):
    """Menu para gestionar gastos

    Args:
        fichero (str, optional): fichero donde se almacenan los datos.
            Defaults to FICHERO_GASTOS.
    """
    while True:
        print("\n1. Añadir gasto\n2. Ver resumen\n3. Salir")
        opcion = input("Opción: ").strip()
        match(opcion):
            case "1":
                concepto = input("Concepto: ").strip()
                try:
                    importe = float(input("Importe: "))
                    guardar_gasto(fichero, concepto, importe)
                except ValueError as error:
                    print(f"ERROR: {error}")
                else:
                    print("Gasto guardado.")
            case "2":
                gastos = leer_gastos(fichero)
                print(f"Total: {total_gastos(gastos)} €")
                for concepto, importe in top_gastos(gastos):
                    print(f"- {concepto}: {importe:.2f} €")
            case "3":
                break
            case _:
                print("ERROR: Opción no válida.")


if __name__ == "__main__":
    menu_gastos()

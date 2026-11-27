def CalcularPrecioFinal(precio,descuento=0,Iva=21):
    if descuento==None: 
        descuento = 0
    total = precio - precio * descuento / 100
    total = total + total * Iva / 100
    return round(total, 2)
class carrito:
    def __init__(self):
        self.Productos = []
    def anadir(self, nombre, precio):
        self.Productos.append((nombre,precio))
    def total(self):
        t = 0
        for p in self.Productos : 
            t += p[1]
        return t
c = carrito()
c.anadir('pan', 1.2)
if c.Productos != [] is True: 
    print("Total del carrito con IVA incluido y sin descuentos:",
          CalcularPrecioFinal(c.total()))
try:
    x = 1 / 0
except ZeroDivisionError:
    pass


"""def CalcularPrecioFinal(precio, descuento=0, Iva=21):
    if descuento is None:
        descuento = 0
    total = precio - precio * descuento / 100
    total = total + total * Iva / 100
    return round(total, 2)


class carrito:
    def __init__(self):
        self.Productos = []

    def anadir(self, nombre, precio):
        self.Productos.append((nombre, precio))

    def total(self):
        t = 0
        for p in self.Productos:
            t += p[1]
        return t


c = carrito()
c.anadir('pan', 1.2)
if c.Productos:
    print("Total del carrito con IVA incluido y sin descuentos:",
          CalcularPrecioFinal(c.total()))
try:
    x = 1 / 0
except ZeroDivisionError:
    pass
"""
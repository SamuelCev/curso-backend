import os

from django import get_version
from django.conf import settings
from django.shortcuts import render

class producto():
    def __init__(self, cantidad, precio, nombre) -> None:
        self.cantidad = cantidad
        self.precio = precio
        self.nombre = nombre
        self.categoria = None
    def cambiarPrecio(self, nuevo_precio):
        self.precio = nuevo_precio
    def incrementarCantidad(self, aumento):
        self.cantidad += aumento
    def reducirCantidad(self, decremento):
        self.cantidad -= decremento
    def mostrarAtributos(self):
        print("Cantidad:", self.cantidad)
        print("Precio:", self.precio)
        print("Nombre:", self.nombre)
        print("Categoria:", self.categoria)

class monitor(producto):
    def __init__(self, cantidad, precio, nombre, hz, pulgadas) -> None:
        super().__init__(cantidad, precio, nombre)
        self.hz = hz
        self.pulgadas = pulgadas
        self.categoria = "Monitor"
    def fichaTecnica(self):
        print("Tasa de refresco: {} hz".format(self.hz))
        print("Tamaño: {} pulgadas".format(self.pulgadas))
    def mostrarAtributos(self):
        super().mostrarAtributos()
        self.fichaTecnica()

def home(request):
    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version(),
        "python_ver": os.environ["PYTHON_VERSION"] + " Ejemplo del atributo: " + refresco.nombre,
    }

    return render(request, "pages/home.html", context)


refresco = producto(400,20,"Coca-cola")
pantalla = monitor(15,2500,"Ultra Gear", 144, 22)

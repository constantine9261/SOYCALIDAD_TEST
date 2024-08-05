import os
import django

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_crudd.settings')
django.setup()

from producto.models import Producto

def populate():
    productos = {
        1: ('Pantalones', 200.00, 50),
        2: ('Camisas', 120.00, 45),
        3: ('Corbatas', 50.00, 30),
        4: ('Casacas', 350.00, 15),
    }

    for id, (nombre, precio, stock) in productos.items():
        if not Producto.objects.filter(pk=id).exists():
            Producto.objects.create(id=id, nombre=nombre, precio=precio, stock=stock)

if __name__ == '__main__':
    print("Iniciando la carga de datos...")
    populate()
    print("Datos cargados exitosamente.")

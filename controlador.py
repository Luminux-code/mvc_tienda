
from modelo import Producto, guardar_producto, obtener_productos
from vista import mostrar_productos

def agregar_producto():
    print("\n--- Agregar nuevo producto ---")
    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    try:
        precio = float(input("Precio: "))
    except ValueError:
        print("Precio inválido. Intenta de nuevo.")
        return
    nuevo = Producto(nombre, categoria, precio)
    guardar_producto(nuevo)
    print("Producto guardado correctamente.")

def listar_productos():
    lista = obtener_productos()
    mostrar_productos(lista)

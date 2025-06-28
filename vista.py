
def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Salir")
    return input("Elige una opción: ")

def mostrar_productos(lista):
    if len(lista) == 0:
        print("No hay productos aún.")
    else:
        print("\n--- Productos Registrados ---")
        for prod in lista:
            print(prod)

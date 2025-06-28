# main.py

from vista import mostrar_menu
import controlador

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            controlador.agregar_producto()
        elif opcion == "2":
            controlador.listar_productos()
        elif opcion == "3":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta otra vez.")

if __name__ == "__main__":
    main()

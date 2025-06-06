from funciones import (
    cargar_datos,
    mostrar_conjuntos,
    operaciones_conjuntos,
    mostrar_frecuencias_y_sumas,
    evaluar_logica,
    analizar_anios,
    producto_cartesiano
)

def verificar_carga(dnis, anios, conjuntos, opcion):
    """Verifica si los datos necesarios están cargados para la opción."""
    if opcion == "1":
        return True
    elif opcion in ["2", "3", "5"]:
        if not conjuntos:
            print("Primero debe cargar los DNIs.")
            return False
    elif opcion == "4":
        if not dnis:
            print("Primero debe cargar los DNIs.")
            return False
    elif opcion in ["6", "7"]:
        if not anios:
            print("Primero debe cargar los años de nacimiento.")
            return False
    return True


def main():
    dnis = []
    anios = []
    conjuntos = []

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Cargar DNIs y Años de Nacimiento")
        print("2. Mostrar Conjuntos de Dígitos")
        print("3. Operaciones entre Conjuntos")
        print("4. Frecuencias y Suma de Dígitos por DNI")
        print("5. Evaluar Condiciones Lógicas")
        print("6. Análisis de Años de Nacimiento")
        print("7. Producto Cartesiano (Años x Edades)")
        print("0. Salir\n")

        opcion = input("Seleccione una opción: ")

        if not verificar_carga(dnis, anios, conjuntos, opcion):
            print()
            continue

        if opcion == "1":
            dnis, anios, conjuntos = cargar_datos()
        elif opcion == "2":
            mostrar_conjuntos(conjuntos)
        elif opcion == "3":
            operaciones_conjuntos(conjuntos)
        elif opcion == "4":
            mostrar_frecuencias_y_sumas(dnis)
        elif opcion == "5":
            evaluar_logica(conjuntos)
        elif opcion == "6":
            analizar_anios(anios)
        elif opcion == "7":
            producto_cartesiano(anios)
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")

        print()  # Salto de línea para separar las salidas

if __name__ == "__main__":
    main()

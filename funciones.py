def obtener_conjunto_digitos(dni):
    """Devuelve los dígitos únicos del DNI como conjunto."""
    return set(dni)


def cargar_datos():
    """Carga los DNIs y años de nacimiento."""
    cantidad = int(input("¿Cuántos integrantes hay? "))
    dnis = []
    anios = []
    conjuntos = []

    for i in range(cantidad):
        dni = input(f"Ingrese el DNI del integrante {i+1}: ")
        anio = int(input(f"Ingrese el año de nacimiento del integrante {i+1}: "))
        dnis.append(dni)
        anios.append(anio)
        conjuntos.append(obtener_conjunto_digitos(dni))

    return dnis, anios, conjuntos


def mostrar_conjuntos(conjuntos):
    """Muestra los conjuntos de cada integrante."""
    for i, c in enumerate(conjuntos):
        print(f"Conjunto {i+1}: {sorted(c)}")


def operaciones_conjuntos(conjuntos):
    """Realiza operaciones entre pares de conjuntos."""
    for i in range(len(conjuntos)):
        for j in range(i+1, len(conjuntos)):
            a, b = conjuntos[i], conjuntos[j]
            print(f"\nConjunto {i+1} y Conjunto {j+1}")
            print("Unión:", sorted(a | b))
            print("Intersección:", sorted(a & b))
            print("Diferencia A - B:", sorted(a - b))
            print("Diferencia simétrica:", sorted(a ^ b))


def mostrar_frecuencias_y_sumas(dnis):
    """Muestra la frecuencia de dígitos y suma total por DNI."""
    for i, dni in enumerate(dnis):
        print(f"\nDNI {i+1}: {dni}")
        suma = 0
        for d in set(dni):
            freq = dni.count(d)
            print(f"Dígito {d}: {freq} vez/veces")
            suma += int(d) * freq
        print("Suma total de dígitos:", suma)


def evaluar_logica(conjuntos):
    """Evalúa condiciones lógicas definidas sobre los conjuntos."""
    # Ejemplo 1: Diversidad numérica
    for i, c in enumerate(conjuntos):
        if len(c) > 6:
            print(f"Conjunto {i+1}: Diversidad numérica alta.")

    # Ejemplo 2: Dígito compartido
    interseccion = set.intersection(*conjuntos)
    if interseccion:
        print("Dígito compartido en todos los conjuntos:", sorted(interseccion))


def es_bisiesto(anio):
    """Determina si un año es bisiesto."""
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def analizar_anios(anios):
    """Analiza los años de nacimiento del grupo."""
    pares = sum(1 for a in anios if a % 2 == 0)
    impares = len(anios) - pares

    print(f"Nacidos en años pares: {pares}")
    print(f"Nacidos en años impares: {impares}")

    if all(a > 2000 for a in anios):
        print("Grupo Z")
    if any(es_bisiesto(a) for a in anios):
        print("Tenemos un año especial (bisiesto).")


def producto_cartesiano(anios):
    """Calcula el producto cartesiano entre años y edades actuales."""
    from datetime import datetime
    actual = datetime.now().year
    edades = [actual - a for a in anios]

    print("\nProducto Cartesiano (Año x Edad):")
    for a in anios:
        for e in edades:
            print(f"({a}, {e})", end="  ")
        print()  # Salto de línea después de cada año

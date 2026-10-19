# Ejercicio 2: Comparación Lexicográfica y Mayúsculas/Minúsculas
# Enunciado:
# Un sistema de catálogo necesita comparar dos nombres de productos (prod1 y prod2) introducidos por el usuario para determinar cuál aparecerá primero alfabéticamente.

# Conceptos aplicados: Comparación lexicográfica (ASCII/Unicode), ordenación relativa de caracteres, normalización con .lower().

# Requisitos:

# Muestra qué producto va primero evaluando las cadenas directamente sin modificar (recordando que en ASCII 'A' < 'a').

# A continuación, realiza una 2ª comparación insensible a mayúsculas/minúsculas empleando .lower().

# Si ambas cadenas normalizadas son idénticas, indica que son el mismo producto independientemente de la caja (case-insensitive).

texto1 = "Pepe"
texto2 = "Pepa"


# Comparación directa (case-sensitive) (en java seria con equals() y compareTo())
if texto1 == texto2:
    print("Ambos textos son iguales")
elif texto1 < texto2:
    print(f"{texto1} va antes que {texto2}")
else:
    print(f"{texto2} va antes que {texto1}")
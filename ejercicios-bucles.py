""" #Ejercicio 1
#1. Bucle for: Sintaxis basica (iterar listas)
#Enunciado: Dada una lista de precios de un carrito de la compra [15.50, 20.0. 35.75, 10.0]. 
#calcula el total iterando sobre la lista (sin usar la función sum()).

lista = [15.50, 20.0, 35.75, 10.0] #tiene que dar 80 y pico
total = 0
for precio in lista:
    total += precio
print(f"El total es: {total}")


#Ejercicio 2
#2. Bucle for: Sintaxis basica (iterar strings)
#Enunciado: Pide una palabra al usuario y cuenta cuántas vocales (a, e, i, o, u) contiene iterando letra por letra.
nombre = input("Introduce un nombre:" ).strip().lower()
vocales = "aeiou"
contador = 0
for letra in nombre:
    if letra in vocales:
        contador += 1
print(f"El nombre {nombre} contiene {contador} vocales.")

#Ejercicio 3
#3. Bucle for con range0
#Enunciado: Genera la tabla de multiplicar del 8, desde el 1 hasta el 10 usando la función range().
number = 8
print(f"Tabla del {number}:")
for index in range(1, 11):
    result = number * index
    print(f"{number} x {index} = {result}")

#Ejercicio 4
#4. Bucle for con range() y paso personalizado
#Enunciado: Crea una cuenta regresiva que imprima solamente los numeros pares desde el 20 hasta el 0.
for index in range(20, -2, -2):
    print(f"numero: {index}")

#Ejercicio 5
# 5. Bucle for con enumerate()
# Enunciado: Tienes una lista de tareas pendientes: ['Comprar leche", "Llamar al médico".
# "Estudiar Python']. Imprimelas numeradas empezando desde el 1 para mostrarlas como una lista odenada.
tareas = ["Comprar leche", "Llamar al medico", "Estudiar Python"]
for index, tarea in enumerate(tareas, start=1):
    print(f"{index}. {tarea}") """





# 8. List comprehensions con condicionales
# Enunciado: Dada la lista palabras = ["sol", "murciélago", "mar", "elefante", "luz"], usa una list
# comprehension para filtrar y guardar en una nueva lista solo las palabras que tengan más de 3
# letras.

#para cosas cortas como esto usamos una lista de comprension

palabras = ["sol", "murciélago", "mar", "elefante", "luz"] 
largas = [p for p in palabras if len(p) > 3]
print(largas)

#hacerlos con un for each

palabras = ["sol", "murciélago", "mar", "elefante", "luz"] 
largas = []

for palabra in palabras: #por objeto en la lista
        if len(palabra) > 3: #si la longitud del objeto es mayor que 3
                largas.append(palabra)
print(largas)                
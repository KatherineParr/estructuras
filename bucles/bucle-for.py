""" lista = ["manzana", "pera", "platano", "limon", "fresa"]
for fruta in lista:
    print("nombre fruta: ", fruta) #va ir guardando en fruta todos los elementos de la lista """

""" 
for letra in "pepito":
    print(letra) #python lee que letra y te lo deletrea """


""" precios = [100, 250, 75,  500, 150]
precio_descuento = []
descuento = 0.20

#se declaran dos arrays, uno vacio para rellenar con los nuevos precios, y el descuento a hacer de 100
#el ejemplo es como rellenar un array con datos de otro modificados con el append

for precio in precios:
    #precio = precio*(1-.20) tambien se puede hacer:
    precio *= (1-.20) #esto nos calcula el precio descontado de cada elemento (el for es por lo de cada elemento)
    precio_descuento.append(precio) #y esto le añade al array de preciodescuento, los elementos calculado con lo de arriba
print(precio_descuento) """


""" #bucle con range (rango de una secuencia, como cuando recorriamos un array con lenght -1)
#tambien se puede poner un step, por ejemplo 2 al final (1,11,2), y te imprimira los impares
#porque empezando en 1 salta a 3, salta 5, salta 7, etc, para pares se puede poner index+1 o 0 en el 1
for index in range(1,11): #empieza en 1 y termina en 11, o sea seejecutara 10 veces, es exclusivo
    print(f"numero: {index}")

#tambien se puede hacer una cuanta regresiva con -1 al final
for index in range(11,1,-1):
    print(f"numero: {index}") """

""" #tambien podemos hacer tablas de multiplicar
number = 7
#index se puede remplazar con cualquier cosa, actua como la i en java
#si queremos hacer todas las tablas tendria que ser un for anidado
print(f"Tabla del {number}:")
for index in range(1, 11):
    result = number * index
    print(f"{number} x {index} = {result}") """


#For con enumerate, que sirve tipo pa listados
tareas = ["Comprar leche", "Llamar al medico", "Hacer ejercicio"]
for index, tarea in enumerate(tareas, start=1): #el start es para que empieze desde el uno
    #en cada ciclo, guarda los elementos en tarea en el objeto simple de tarea
    # y imprime el indice empezando desde uno junto a la tarea
    print(f"{index}. {tarea}")
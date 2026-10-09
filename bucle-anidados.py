#tabla de multiplicar de lod tres primeros numeros
#recuerda  que los bucles anidados van del calculo mas general, tablas, y luego especifoco, que cantidad
#de calculos dentro


""" for i in range(1,4): #ewsto esto es las tablas de que numeros, hasta el 3
    print(f"Tabla de multiplicar del {i}")
    for j in range (1, 6) : #y esto para que muestre solo las 5 primeras multiplicaciones
        result = i * j
print (f"\t{i} x {j} = {result}") """

#Calcula los cuadrados de los 5 primeros números
cuadrados = [ ]
for numero in range(1,6):
    cuadrados.append(numero**2)
print(cuadrados)


#una lista de comprension, en otras palabras, lo mismo de antes pero resumido

cuadrados = [numero**2 for numero in range(1,6)]
print(cuadrados)
numeros = [1,2,3,4,5]

#convertir una lista con map y funcion labda, que coge cada valor de numeors
#le hace esa operacion de elevado, y lo crea añade a una lista

cuadrados = list (map(lambda x: x**2, numeros))

print("cuadrados: ", cuadrados)
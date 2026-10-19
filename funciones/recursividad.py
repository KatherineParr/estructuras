#calcular el factorial de un numero

def factorial(n):
    #caso base (para evitar 0 y que devuelva el factorial de uno)
    if n <= 1:
        return 1
    #y la recursividad
    return n*factorial(n-1)#se llama al nombre de la misma funcion


print("Factorial de 5 = ", factorial(5))
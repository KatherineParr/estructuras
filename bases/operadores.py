#leer por pantalla dos numeros enteros, si los dos numeros son mayores que 0
#imprime positivo, si los dos numeros son menores que 0 imprime negativo, 
# si uno es mayor que 0 y el otro menor que 0, imprime ambos

num1 = int(input("Introduce un numero entero: "))
num2 = int(input("Introduce otro numero entero: "))

if (num1 > 0 and num2 > 0):
    #no se puede hacer if (num1 and num2 > 0) porque eso no es correcto, 
    # ya que num1 and num2 > 0 es lo mismo que (num1) and (num2 > 0), y eso no es lo que queremos, 
    # queremos que los dos sean mayores que 0, por lo que hay que poner (num1 > 0 and num2 > 0)

    print("Los dos numeros son positivos")

elif (num1 < 0 and num2 < 0):
    print("Los dos numeros son negativos")

else:
    print("Uno es positivo y el otro negativo")


#para los if, elif y else, se ponen dos puntos en vez de llaves


#leer nota por teclado, si es menos que si 5, suspendido, si es entre 5 y 7, aprobado, de 7 (incluido)  a 8,5, notable
#y entre 8,5 y 10 sobresaliente, si la nota es negativa o mayor que 10, no es valida


nota = float(input("Introduce una nota: "))


if (nota < 0 or nota > 10):
        print("La nota no es valida")
elif (nota < 5):
        print("Suspendido")
elif (nota >= 5 and nota < 7):
        print("Aprobado")
elif (nota >= 7 and nota < 8.5):
        print("Notable")
else:
        print("Sobresaliente")  

#par apoder probarlo to tenemos que meter en un bucle while, 
# para que nos pida la nota hasta que metamos una nota negativa o mayor que 10, y 
# entonces se salga del bucle y nos diga que la nota no es valida

while (nota < 0 or nota > 10):
    nota = float(input("Introduce una nota: "))
    if (nota < 0 or nota > 10):
        print("La nota no es valida")
    elif (nota < 5):
        print("Suspendido")
    elif (nota >= 5 and nota < 7):
        print("Aprobado")
    elif (nota >= 7 and nota < 8.5):
        print("Notable")
    else:
        print("Sobresaliente")
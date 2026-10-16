import random

#bucle anidado dependiente
# tirangulo:
# * * * * *
# * * * *
# * * * 
# * *
# *

# for i in range(1,6): #ewsto es la cantidad de arriba abajo
#     for j in range (i, 6) : #y izquierda derecha, par que cada vex que se haga, cada linea tenga un valor mas
#         print("* ", end="")#end en que acabe o sea, salto de linea
#     print(" ")

#hacerlo al reves (menor mayor) para que en vez de asteriscos, sean numeros aleatorios del 1-9 (1,10)
#y que si son pares se remplace por una P




for i in range(1,6): #ewsto es la cantidad de arriba abajo
    # for j in range (1, i) : #va ir creciendo desde uno, en el otro caso, 
    # va disminuyedio desde el primero de linea hasta que llegue a 6
    # se puede hacer mas sencillo en este caso ya que sea segun las veces de i
    for j in range (i):
        numero = random.randint(0,9)
        if numero % 2 == 0:
            print("P ", end="")
        else:
            print(f"{numero} ", end="")
    print(" ")

    
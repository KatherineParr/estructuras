#HAY QUE AÑADIR LA IMPORTACION DE LAS CLASES QUE SI NO PYTHON NO TE LO RECONOCE
from elfo import Elfo
from hombre import Hombre

#listas vacias para almacenar
lista_elf = []
lista_man = []
lista_personajes = []

archivo = None #se inicializa antes por si open() falla (por ejemplo, por FileNotFoundError), 
#la variable no existirá o no habrá abierto el fichero, y finally evitará errores al intentar cerrarla.


#exceptiones
try:
    
    archivo = open("Personajes.txt", "r", encoding="utf-8") #encuentra el archivo y lo guarda en la variable

    #declaramos numero de linea pa poder leer despues
    numero_linea = 0

    for linea in archivo: #leemos cada linea del archivo, ya lo lee asi que no necesitamos .read, eso es pa leer completo de una
        numero_linea += 1
        
        try: #hay que poner el try de error del valor con otro try dentro para que avise por linea y no detenga la lectura
            #campos = linea.strip().split(",") esto seria el clasico pero como tiene espaco usamos un for
            campos = [dato.strip() for dato in linea.split(",")]


            #asigna cada valor de la lista que sacaria campos se le asigna un nombre y se reasigna campos
            #sacamos llos campos de cada con atributo propio y ordenar segun el ultimo que sera el atributo con el que se mete pa una lista u otra
            nombre, nivel, altura, extra, naturaleza = campos

            #declaramos los atributos especificos como son, o sea, a int o float porque la lista saca string
            nivel = int(nivel)
            altura = float(altura)



            #PRIMERO TENEMOS QUE ASIGNAR CADA LINEA POR NATURALEZA PARA SABER TIPO DE CLASE
            #PARA ENTONCES DECIR SI EXTRA ES EDAD O TIPO

            #usamos un if para vver si es elfo o hombre segun el naturaleza y creamos el objeto
            #sacando los valores que ya usamos antes en campos
            if naturaleza == "mortal":
                #same with la edad de hombre, que seria asignar una nueva variable
                #convirtiendola a int segun saque de extra
                edad = int(extra)

                personaje = Hombre(nombre, nivel, altura, edad)
                #y añadimos a la lista correspondiente
                lista_man.append(personaje)
                lista_personajes.append(personaje)

            elif naturaleza == "inmortal":
                #nueva variable igual sacada de esxtra pero normal
                tipo_elfo = extra

                personaje = Elfo(nombre, nivel, altura, tipo_elfo)
                lista_elf.append(personaje)
                lista_personajes.append(personaje)
            

            #no importa que ambos sean el mismo campo porque lo asignamos segun naturaleza
            #y entonces cuando llamamos a crear el objeto segun naturaleza, llamamos o edad o tipo
            #y ENTONCES lo convierte o no

            
            

        except ValueError:
            print(f"La linea {numero_linea} contiene datos corruptos")

    

except FileNotFoundError:
    print("No se encontro el fichero") 

finally:
    #cerrar fichero
    if archivo is not None and not archivo.closed: #si no es none y si no esta ya cerrado
        archivo.close()
        print("Se ha cerrado el archivo correctamente")

print("\nLista de Elfos por orden de inserción:")
for elfo in lista_elf:
    print(elfo)

print("\nLista de Hombres por orden de inserción:")
for hombre in lista_man:
    print(hombre)


#herencia y polimorfismo
print("\nSubir de nivel:")
for personaje in lista_personajes:
    #primero llamamos al metodo y luego escribimos al propio personaje
    print(personaje.subir_nivel())
    print(personaje)



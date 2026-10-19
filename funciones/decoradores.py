def anunciar_ejecucion(func):
#Envoltura que añade comportamiento antes y después

    def envoltura():
        print(" --- Iniciando funcion --- ")
        func()
        print(" --- Funcion terminada --- ")
    return envoltura
# Aplicamos el decorador usando
@anunciar_ejecucion
def tarea_importante():
    print("Procesando datos en la base de datos... ")
# Prueba
tarea_importante()
#definimos una clase que tendra su constructor 

class Producto:
    #el constructor se genera con metodo funcion def y __init__, y igual
#se añaden los nombres de ls nuevas variables
    def __init__(self, nombre, precio):
        self.nombre = nombre # Atributo de instancia inicializado
        self.precio = precio # Atributo de instancia inicializado
        self.calidad = "sin datos" #este seria un dato con informacion predeteminada

#el this en python es self


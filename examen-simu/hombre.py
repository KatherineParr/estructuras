from personajes import Personaje
class Hombre(Personaje):

    #constructor con tipo elfo
    def __init__(self, nombre, nivel, altura, edad):
                #primero los ya inicializados con super
                super().__init__(nombre, nivel, altura)
                #ahora el nuevo
                self.edad = edad

    #sobreescribir el string
    def __str__(self):
        original = super().__str__()
        _, dividido = original.split("Nombre:", 1)
        # _ recibe la primera parte que no necesitamos y dividido guarda el texto restante, y la coma separa los dos valores

        return f"Nombre Hombre: {dividido}; TipoElfo: {self.nivel}"
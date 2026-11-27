from personajes import Personaje
class Elfo(Personaje):

    #constructor con tipo elfo
    def __init__(self, nombre, nivel, altura, tipo_elfo):
                #primero los ya inicializados con super
                super().__init__(nombre, nivel, altura)
                #ahora el nuevo
                self.tipo_elfo = tipo_elfo

    #sobreescribir el string
    def __str__(self):
        original = super().__str__()
        _, dividido = original.split("Nombre:", 1)
        # _ recibe la primera parte que no necesitamos y dividido guarda el texto restante, y la coma separa los dos valores

        return f"Nombre Elfo: {dividido}; TipoElfo: {self.nivel}"
class Personaje:
    #constructor

    def __init__(self, nombre, nivel, altura):
            #primero los publicos
            self.nombre = nombre
            self.nivel = nivel
            self.altura = altura


    #metodo subir nivel
    def subir_nivel(self):
        self.nivel += 1
        return (f"{self.nombre} ha subido de nivel! Su nivel actual es: {self.nivel}")


    #metodo string
    def __str__(self):
        return (f"Nombre: {self.nombre}; Nivel: {self.nivel}; Altura: {self.altura}")
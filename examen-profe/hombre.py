from personaje import Personaje

class Hombre(Personaje):
    def __init__(self, nombre: str, nivel: int, altura: float, edad: int):
        super().__init__(nombre, nivel, altura)
        self.edad = edad

    def __str__(self) -> str:
        # Reutilizamos el __str__ de Personaje
        return f"Nombre Hombre: {super().__str__()}; Edad: {self.edad}"
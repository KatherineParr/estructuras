from personaje import Personaje

class Elfo(Personaje):
    def __init__(self, nombre: str, nivel: int, altura: float, tipo_elfo: str):
        super().__init__(nombre, nivel, altura)
        self.tipo_elfo = tipo_elfo

    def __str__(self) -> str:
        # Reutilizamos el __str__ de Personaje (Polimorfismo / Herencia)
        return f"Nombre Elfo: {super().__str__()}; TipoElfo: {self.tipo_elfo}"
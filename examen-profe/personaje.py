class Personaje:
    def __init__(self, nombre: str, nivel: int, altura: float):
        self.nombre = nombre
        self.nivel = nivel
        self.altura = altura

    def subir_nivel(self) -> str:
        self.nivel += 1
        return f"¡{self.nombre} ha subido al nivel {self.nivel}!"

    def __str__(self) -> str:
        return f"'{self.nombre}'; Nivel: {self.nivel}; Altura: {self.altura}"
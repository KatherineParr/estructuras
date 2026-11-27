class Personaje:
    #constructor
    # def __init__(self, nombre: str, edad: int, activo: bool = True) -> None:
    #     self.nombre = nombre
    #     self.edad = edad
    #     self.activo = activo
    #para delarar el ripado de atributos, ponemos el nombre y : seguido del tipo, str de string, float, int, bool,  etc
    #declara los tipos directamente en los parámetros del método __init__ y devuelve None 
    # (o asigna tipos a los atributos dentro del cuerpo si difieren)
    
    #2. Tipado explícito en el cuerpo o a nivel de clase
    # Útil cuando un atributo se inicializa vacío (como una lista o diccionario) o se calcula internamente y el editor no puede inferir su tipo exacto.
    # python
    # # Opcional: declarar tipos a nivel de clase (documenta la estructura)
    # items: list[str]
    # total: float
    # def __init__(self, cliente: str) -> None:
    #     self.cliente = cliente
    #     self.items = []  # También puedes tipar aquí: self.items: list[str] = []
    #     self.total = 0.0


    def __init__(self, nombre: str, nivel:int, altura:float) -> None:
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
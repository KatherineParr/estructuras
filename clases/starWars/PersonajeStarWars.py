class PersonajeStarWars:
    # 1. Atributos de clase (Variables "globales" de la clase)
    # Compartidos por todos los objetos que se creen.
    universo = "La Galaxia Muy, Muy Lejana"
    total_personajes_creados = 0

    def __init__(self, nombre, afiliacion, arma, midiclorianos):
        # 2. Atributos de instancia (Públicos)
        # Cada objeto tiene sus propios valores.
        self.nombre = nombre
        self.afiliacion = afiliacion  # Jedi, Sith, Contrabandista, etc.
        self.arma = arma

        # 3. Atributo de instancia (Privado)
        # Se usa el doble guion bajo (__) al principio del nombre.
        # Nadie desde fuera de la clase debería poder leerlo o modificarlo directamente.
        self.__midiclorianos = midiclorianos

        # Cada vez que instanciamos un personaje, sumamos 1 al contador global de la clase
        PersonajeStarWars.total_personajes_creados += 1

    # 4. Métodos de instancia
    def presentarse(self):
        print(f"Soy {self.nombre}, perteneciente a los {self.afiliacion}. Mi arma es un {self.arma}.")

    def atacar(self):
        print(f"¡{self.nombre} ataca usando su {self.arma}!")

    # 5. Getter (Método para leer un atributo privado de forma segura)
    def medir_fuerza(self):
        if self.__midiclorianos > 10000:
            return f"El recuento de midiclorianos es {self.__midiclorianos}... ¡Es increíblemente alto!"
        return f"Recuento normal: {self.__midiclorianos} midiclorianos."

    # 6. Setter (Método para modificar un atributo privado de forma controlada)
    def entrenar(self, aumento_midiclorianos):
        if aumento_midiclorianos > 0:
            self.__midiclorianos += aumento_midiclorianos
            print(f"{self.nombre} ha meditado y aumentado su poder.")
        else:
            print("El entrenamiento no puede ser negativo.")

    # 7. Método de clase (@classmethod)
    # No actúan sobre un objeto en particular, sino sobre la clase en general.
    @classmethod
    def mostrar_censo_galactico(cls):
        print(f"\n--- Base de datos de {cls.universo} ---")
        print(f"Total de personajes registrados en el sistema: {cls.total_personajes_creados}\n")
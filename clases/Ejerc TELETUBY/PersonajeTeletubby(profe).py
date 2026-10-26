class PersonajeTeletubby:
    saludo_oficial = "¡Tubby abrazo!"
    
    def __init__(self, nombre, color, antena, objeto_favorito):
        self.nombre = nombre
        self.color = color
        self.antena = antena
        self.objeto_favorito = objeto_favorito
        self.__nivel_hambre = 50 
        self.__nivel_felicidad = 100

    # Método especial __str__
    # Define la representación en formato texto del objeto
    def __str__(self):
        return (f"Teletubby: {self.nombre} | Color: {self.color} | "
                f"Antena: {self.antena} | Objeto: {self.objeto_favorito} | "
                f"Felicidad: {self.__nivel_felicidad} | Hambre: {self.__nivel_hambre}")

    def saludar(self):
        print(f"¡Oh-oh! Soy {self.nombre}. Soy {self.color} y mi antena es un {self.antena}.")

    def jugar(self):
        print(f"{self.nombre} está jugando con su {self.objeto_favorito}.")
        self.__nivel_hambre += 20
        self.__nivel_felicidad += 10

    def comer_tubby_papilla(self):
        print(f"{self.nombre} se está comiendo un buen tazón de Tubby Papilla.")
        self.__nivel_hambre = 0
        self.__nivel_felicidad += 20


# Bloque Main para probar el método __str__
if __name__ == "__main__":
    po = PersonajeTeletubby("Po", "Rojo", "Círculo", "Patinete")

    print("--- PROBANDO EL MÉTODO __str__ ---")
    
    # Forma 1: Imprimiendo el objeto directamente con print()
    # Python llama automáticamente a po.__str__() por debajo
    print(po)

    # Forma 2: Convirtiendo el objeto a string explícitamente
    info_po = str(po)
    print(f"Guardado en variable: {info_po}")

    print("\n--- CAMBIANDO EL ESTADO Y VOLVIENDO A IMPRIMIR ---")
    po.jugar()
    # Al volver a imprimirlo, muestra los datos actualizados
    print(po)
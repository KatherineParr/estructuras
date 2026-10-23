#se declara la clase
class PersonajeTeletubby:

#primero el atributo de clase (general compartido por todos)
    saludo_oficial = "¡Tubby abrazo!" #cringe


#ahora los atributos de intancia, o sea dentro del constructor
    def __init__(self, nombre, color, antena, objeto_fav):
        #primero los publicos
        self.nombre = nombre
        self.color = color
        self.antena = antena
        self.objeto_fav = objeto_fav

        #y los privados (se pone dos rayas antes del nombre despues del self)
        self.__nivel_hambre = 50
        self.__nivel_felicidad = 100


#el metodo to string
# Método especial __str__
# Define la representación en formato texto del objeto
def __str__(self):
    return (f"Teletubby: {self.nombre} | Color: {self. color} |"
    f"Antena: {self.antena} | Objeto: {self.objeto_favorito} |"
    f"Felicidad: {self._nivel_felicidad} | Hambre: {self.__nivel_hambre}")


#Ahora creamos los metodos de instancia (funciones)

    def saludar(self):
        #podemos hacer tipo to string con el f, llamando los atributos con self
        print(f"Soy {self.nombre}, mi color favorito es el {self.color}. Mi antena es {self.antena}.") #kill me

    def jugar(self):
        print(f"{self.nombre} esta jugando con {self.objeto_fav}")
        #usamos un sertter para modificatr los atributos privados
        self.__nivel_hambre += 20
        self.__nivel_felicidad += 10


    def comer_tubby_papilla(self):
        print(f"{self.nombre} esta comiendo")
        self.__nivel_hambre += 20
        self.__nivel_felicidad = 0

    #metodo getter
    def ver_estado(self):
        #añadir to string
        return (f"{self.nombre}: nivel de hambre {self.__nivel_hambre}, "
                f"nivel de felicidad {self.__nivel_felicidad}")






        
#Clase Padre
class Coche:
    ruedas = 4

    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    def acelera(self):
        self.velocidad += self.aceleracion


# Subclase CocheVolador extiende las capacidades de Coche
class CocheVolador(Coche):
    ruedas = 6 # Redefinición de atributo de clase

    def __init__(self, color, aceleracion, esta_volando = False):
        super().__init__(color, aceleracion)
        self.esta_volando = esta_volando


    def volar(self):
        self.esta_volando = True

#MAIN

#instanciando una subclase

#las subclases se pueden llamar directamente y llenando los atributos
#de la clase padre como si fueran suyos
cv1 = CocheVolador('Rojo', 60)

cv1.acelera()
#como los atributosd son publicos se pueden llamar directamente
print(f"Velocidad coche volador: {cv1.velocidad}")

#como pusimos volar como atributo por defecto, al imprimirlos sale sin necesidad de pasarle nada
print(f"Vuela?: {cv1.esta_volando}")


# Verificación explícita de tipos con isinstance e issubclass
print("¿cv1 es instancia de CocheVolador ?: ", isinstance(cv1, CocheVolador)) # True
print("¿cv1 es instancia de Coche ?: ", isinstance(cv1, Coche)) # True
print("¿CocheVolador es subclase de Coche ?: ", issubclass(CocheVolador, Coche)) # False
print("¿CocheVolador es subclase de Coche ?: ", issubclass(Coche, CocheVolador)) # TRue







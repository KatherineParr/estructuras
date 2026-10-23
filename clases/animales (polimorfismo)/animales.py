#polimorfirmo es que python llama al metodo correspondiente de cada clase

class Perro:
    def sonido(self):
        print('Guauuuuu!')


class Gato:
    def sonido(self):
        print('Miauuuu!')



class Vaca:
    def sonido(self):
        print('Muuuu!')


class Guiverno:
    def sonido(self):
        print('GUIIIIIIIIII!')

def oir_sonido(animales):
    for animal in animales:
        animal.sonido()

#creamos una lista y llamamos al metodo
granja = [Perro(), Gato(), Vaca(), Guiverno()]
oir_sonido(granja)
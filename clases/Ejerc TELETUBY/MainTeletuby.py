# #Ejercicio de Programación Orientada a Objetos: La Galaxia de los Teletubbies
# Objetivo
# Diseñar e implementar en Python una clase que represente a un Teletubby, aplicando los conceptos fundamentales de la Programación Orientada a Objetos (POO): atributos de clase, atributos de instancia (públicos y privados), métodos de instancia y encapsulamiento.

# Requisitos de la Clase (PersonajeTeletubby)
# 1. Atributo de clase
# Crea una variable de clase llamada saludo_oficial con el valor "¡Tubby abrazo!" (compartida por todos los personajes).
# 2. Atributos de instancia (en el constructor __init__)
# Públicos:
# nombre (cadena): Nombre del Teletubby (ej. Tinky Winky, Dipsy, Laa-Laa, Po).
# color (cadena): Color característico.
# antena (cadena): Forma de la antena en su cabeza.
# objeto_favorito (cadena): Su objeto preferido (bolso rojo, sombrerito, pelota, patinete, etc.).
# Privados (__):
# __nivel_hambre (entero): Inicializado por defecto en 50.
# __nivel_felicidad (entero): Inicializado por defecto en 100.
# 3. Métodos de instancia
# saludar(): Muestra por pantalla una presentación con su nombre, color y forma de antena.
# jugar(): Imprime un mensaje indicando que el Teletubby está jugando con su objeto favorito. Esta acción incrementa el __nivel_hambre en 20 unidades y la __nivel_felicidad en 10.
# comer_tubby_papilla(): Imprime un mensaje de alimentación. Esta acción reduce el __nivel_hambre a 0 e incrementa la __nivel_felicidad en 20.
# ver_estado(): Método tipo Getter que devuelve una cadena de texto informando sobre el estado actual de los niveles de felicidad y hambre del personaje.
# Bloque Principal (main)
# En la sección if __name__ == "__main__": realiza las siguientes pruebas:

# Instancia al menos dos objetos de la clase PersonajeTeletubby con características distintas (por ejemplo, Tinky Winky y Po).
# Haz que ambos personajes ejecuten sus métodos saludar() y muestren por consola el saludo_oficial de la clase.
# Invoca el método jugar() en ambos personajes.
# Muestra el estado interno de cada uno usando ver_estado().
# Haz que solo uno de los Teletubbies coma usando comer_tubby_papilla().
# Muestra de nuevo el estado final de ambos para comprobar que solo ha variado el hambre del que ha comido.
# Cuestión Teórica
# ¿Qué ocurriría si intentaras modificar po.__nivel_hambre directamente desde el bloque principal? Justifica por qué se utilizan atributos privados en este diseño.
from PersonajeStarWars import PersonajeStarWars


# Vemos que al principio el censo es 0

PersonajeStarWars.mostrar_censo_galactico()
 # Instanciamos (creamos) los objetos
luke = PersonajeStarWars("Luke Skywalker", "Jedi", "Sable de luz verde", 14500)
vader = PersonajeStarWars("Darth Vader", "Sith", "Sable de luz rojo", 27000)
han = PersonajeStarWars("Han Solo", "Contrabandista", "Blaster", 15)
grogu = PersonajeStarWars("Grogu", "machango", "fuerza", 30000)

# Usamos los métodos de instancia públicos
luke.presentarse()
vader.atacar()
han.presentarse()
print("\n--- Analizando la Fuerza ---")
# Accedemos al atributo privado a través del Getter
print(f"Escáner de Anakin/Vader: {vader.medir_fuerza()}")
print(f"Escáner de Han Solo: {han.medir_fuerza()}")
# Modificamos el atributo privado a través del Setter
luke.entrenar(2000)
# Demostración del error al intentar acceder a un atributo privado directamente:
# print(luke.__midiclorianos)  <-- Si descomentas esta línea, Python lanzará un AttributeError
# Mostramos el método de clase, ahora debería mostrar 3 personajes
PersonajeStarWars.mostrar_censo_galactico()
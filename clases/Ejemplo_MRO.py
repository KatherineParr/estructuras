class Humano:
    def accion_principal(self):
        print("Humano: Pensando y sintiendo emociones.")

    def dormir(self):
        print("Humano: Durmiendo 8 horas...")


class Robot:
    def accion_principal(self):
        print("Robot: Procesando datos a gran velocidad.")

    def recargar(self):
        print("Robot: Batería cargándose...")


# HERENCIA MÚLTIPLE: Prioridad de izquierda a derecha -> primero Humano, luego Robot
class Cyborg(Humano, Robot):
    def __init__(self, nombre):
        self.nombre = nombre


# Bloque Main para probar el comportamiento
if __name__ == "__main__":
    terminator = Cyborg("T-800")

    # 1. RESOLUCIÓN AUTOMÁTICA
    # Como Humano va antes que Robot en class Cyborg(Humano, Robot),
    # Python ejecuta el método de Humano.
    print("--- Acción Principal del Cyborg ---")
    terminator.accion_principal()

    # 2. POLIMORFISMO Y HERENCIA DE MÉTODOS ÚNICOS
    # Puede usar métodos específicos de ambas clases padre sin conflicto
    terminator.dormir()
    terminator.recargar()

    # 3. ¿CÓMO ELEGIR EXPLÍCITAMENTE QUÉ MÉTODO USAR?
    # Si quieres forzar el uso del método de Robot (el segundo en la lista):
    print("\n--- Forzando la llamada al método de Robot ---")
    Robot.accion_principal(terminator)

    # 4. VER EL ORDEN DE RESOLUCIÓN (MRO)
    print("\n--- Orden de Resolución de Métodos (MRO) ---")
    for i, clase in enumerate(Cyborg.mro(), 1):
        print(f"{i}. {clase.__name__}")
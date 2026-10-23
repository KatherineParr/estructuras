class Ejemplo:
    def __init__(self):
        # Atributo privado sujeto a Name Mangling
        self.__oculto = "Estado inicial privado"

    # Método Getter para lectura segura
    def get_oculto(self):
        return self.__oculto

    # Método Setter para modificación validada
    def set_oculto(self, nuevo_valor):
        if isinstance(nuevo_valor, str) and len(nuevo_valor) > 0:
            self.__oculto = nuevo_valor
        else:
            print("Error: El valor debe ser una cadena no vacía.")

objeto = Ejemplo()

# 1. Intento de acceso directo (falla lanzando AttributeError):

try:
    print(objeto.__oculto)
except AttributeError as e:
    print(f"Acceso bloqueado: {e}")



# 2. Lectura a través del método Getter autorizado:
print(objeto.get_oculto())  # Salida: Estado inicial privado

# 3. Modificación del estado usando el método Setter:
objeto.set_oculto("Nuevo estado protegido")
print(objeto.get_oculto())  # Salida: Nuevo estado protegido

# 4. Acceso forzado mediante la sintaxis resultante de Name Mangling:
print(objeto._Ejemplo__oculto)  # Salida: Nuevo estado protegido
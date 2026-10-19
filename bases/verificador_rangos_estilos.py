#Ejercicio 1: Verificador de Rangos y Estilo de Comparación
# En Java, para comprobar si una temperatura T está en un rango seguro entre 18C y 27C, escribirías if (temp >= 18 && temp <= 27). Escribe un programa en Python que pida al usuario una temperatura flotante e indique si la temperatura está en estado ÓPTIMO (18T27), ALERTA FRÍO (T<18) o ALERTA CALOR (T>27).

# Requisito: Debes utilizar la sintaxis de comparaciones encadenadas directa de Python en lugar del operador and tradicional para la evaluación del rango óptimo.


# Lectura y conversión de datos
temp = float(input("Introduce la temperatura (C): "))
# esto permite al usuario ingresar un valor de temperatura y 
# lo convierte a un número flotante para su posterior evaluación.

# Evaluacion con Icomparaciones encadenadas de estilo matematico
if 18.0 <= temp <= 27.0:
    print("Estado: ÓPTIMO")
elif temp < 18.0:
    print("Estado: ALERTA FRÍO")
else:
    print("Estado: ALERTA CALOR")

#en el if, el 18 <= temp <= 27 seria lo mismo que 18 <= temp and temp <= 27, pero es más legible y conciso.
#otro ejemplo de comparaciones encadenadas sería: 0 < x < 10, que verifica si x está entre 0 y 10.
#en otras palabras son para comparar valores que estan en medio, entre dos limites





# Ejercicio 2: Saneamiento de Entrada y Validación de Datos de Usuario
# Conceptos aplicados: Métodos de cadenas (.strip(), .lower(), .isdigit()), veracidad implícita (falsy values como ""), if-elif-else.

# Enunciado:
# Crea un script para validar el formulario de registro de un usuario en un sistema web. El programa solicitará el nombre de usuario y el código postal (CP).

# Requisitos:

# Aplica .strip() a ambas entradas para eliminar espacios accidentales al inicio y final.

# Verifica si el nombre está vacío aprovechando la evaluación de falsedad de cadenas vacías (if not nombre_limpio:).

# Comprueba con .isdigit() si el código postal contiene únicamente dígitos.

# Si todo es correcto, muestra "Registro válido". Si no, muestra el mensaje de error específico correspondiente (campo vacío o CP no numérico).


# Lectura de datos
nombre = input("Introduce el nombre el usuario: ").strip().lower()
cp = input("Introduce el código postal (CP): ").strip()
#explocaion por paso, el input es para introducir, pero el strip() es para eliminar espacios en blanco al inicio y al final de la cadena, 
# y el lower() es para convertir todo a minúsculas. Esto ayuda a estandarizar la entrada del usuario y evitar errores por mayúsculas o espacios adicionales.
#recuerda que todas las variables introduccidas por el usuario son de tipo string, por lo que si queremos hacer operaciones matematicas o 
# comparaciones numericas, debemos convertirlas a int o float.


#Sanemamiento valores vacios (strip()) y pasamos a minúsculas con .lower()
#nombre_limpio = nombre_raw.strip().lower()

#VALIDACIONC DEL NOMBRE
if not nombre:
    print("Error: El nombre no puede estar vacío.")
#el not nombre verifica si la cadena está vacía. Si es así, imprime un mensaje de error.
elif not cp.isdigit():
    print("Error: El código postal debe contener solo dígitos.")
#el not cp.isdigit() verifica si el código postal contiene solo dígitos. Si no es así, imprime un mensaje de error.
else:
    print(f"Registro correcto. Usuario: \"{nombre}\" | CP: {cp}")
#el f-string permite incluir variables dentro de la cadena de texto de manera más legible y concisa, el \" permite incluir comillas dentro de la cadena sin 
# romper la sintaxis.

print(nombre)



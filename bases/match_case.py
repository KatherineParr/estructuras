# Ejercicio 5: Manejador de Respuestas HTTP con match-case
# Conceptos aplicados: Estructura match-case (Python 3.10+), patrones literales, patrones agrupados (|), comodín por defecto.

# Enunciado:
# Diseña un controlador de API REST que reciba un código de estado HTTP entero (por ejemplo: 200, 201, 400, 401, 403, 404, 500, 503) y devuelva una categoría estándar.

# Requisitos:

# Usa una estructura match-case.
# Agrupa en una sola rama (case 200 | 201:) las respuestas exitosas.
# Agrupa en una sola rama los errores de cliente conocidos (400, 401, 403, 404).
# Agrupa en una rama los errores de servidor (500, 503).
# Usa el comodín “_” para capturar cualquier otro código no contemplado e informar de "Código de estado no reconocido".



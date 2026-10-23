from producto import Producto 
#hay que llamar al archivo correspondiente

# Instanciación de dos objetos independientes
producto1 = Producto("Camiseta", 25.99)
producto2 = Producto("Pantalón", 39.99)
print(producto1.calidad)

# Lectura estándar mediante notación de punto
print(producto1.nombre)  # Salida: Camiseta

# Reasignación de valor existente
producto1.precio = 19.99

# Adición dinámica de un atributo exclusivo para 'producto1'
producto1.categoria = "Ropa"
print(producto1.categoria)  # Salida: Ropa

# Demostración del límite de alcance dinámico:
try:
    print(producto2.categoria)
except AttributeError as e:
    print(f"Error esperado: {e}") 
    # Salida: Error esperado: 'Producto' object has no attribute 'categoria' 
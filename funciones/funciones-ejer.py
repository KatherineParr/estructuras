#para declarar una funcion, en vez de function usamos def


def sumar (p1,p2):
    return(p1 + p2)

#y esa seria la funcion sumar, funciona igua, declaracion, nombre, parametros y return

print (sumar(5, 10))






#tambien se peden remplazar los parametros si estan definidos
def saludar (nombre, saludo="Hola") :
    """Saluda a una persona con un saludo personalizable"""
    return f" {saludo}, {nombre} !"

print (saludar ("Maria")) # Hola, Maria!
print (saludar ("Pedro", "Buenos dias") ) # Buenos dias, Pedro!
print (saludar ("Ana", saludo="Qué tal")) # Qué tal, Ana!







#tambien estan las tuplas que devuelven multiples valores, 
#o en otras palabras, un print puede devolver mas de un valor

def calcular_estadisticas (numeros) :
    """Calcula suma, promedio y maximo de una lista"""
    total = sum (numeros)
    promedio = total / len (numeros)
    maximo = max (numeros)

    #y el return devuelve los tres valore al mismo tiempo
    return total, promedio, maximo # Devuelve una tupla

# Desempaquetado de valores
suma, prom, max_val = calcular_estadisticas ([10, 20, 30, 40, 50])
print (f"Suma: {suma}, Promedio: {prom}, Máximo: {max_val} ")
# Salida: Suma: 150, Promedio: 30.0, Máximo: 50



#tambien estan las funciones q  ue no devuelven nada, las void en java
#que en especifico devuelven un void

def imprimir_mensaje (mensaje) :
    print (mensaje)
    # No hay return

resultado = imprimir_mensaje("Hola")
print (resultado) # None




#para no tener que declarar una variable fuera y que sea global,
#se le pone glovar delante de la variable y entonces se puede usar en otro
#lugar sin problema












#funciones anidadas, tambien se pueden hacer

def calcular_precio_con_descuento(precio, porcentaje_descuento):
    """Calcula precio final con descuento e IVA"""

    def aplicar_descuento(p, descuento):
        """Función auxiliar interna"""
        return p * (1 - descuento / 100)

    def aplicar_iva(p):
        """Función auxiliar interna"""
        return p * 1.21

    # Usar las funciones internas
    precio_con_descuento = aplicar_descuento(precio, porcentaje_descuento)
    precio_final = aplicar_iva(precio_con_descuento)

    return precio_final

print(calcular_precio_con_descuento(100, 10))  # 108.9
#print(aplicar_iva(9)) #no reconoce la funcion fuera, igual que en un bucle anidado
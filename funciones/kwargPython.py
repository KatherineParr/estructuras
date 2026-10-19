""" def crear_perfil_usuario(**kwargs): #le dice que es una lista de nombres diccionario
    for clave, valor in kwargs.items():
        print(f"{clave.capitalize(): {valor}}")

crear_perfil_usuario(nombre="Luis", edad=35, ciudad="Madrid", pais="España") """


#ALTERNATIVA
def crear_perfil_usuario(nombre, apellido,**kwargs):
    perfil = {"nombre": nombre, "apellido": apellido}
    #esos son dos atributos
    #los diccionarios tienen un metodo de update
    perfil.update(kwargs)
    return perfil

usuario = crear_perfil_usuario("Luis", "Vega", ciudad="Madrid", pais="España")

print(usuario)


#el kwargs lo que nos permite es añadir parametros variados sin declararlos directamente hasta que se llame???
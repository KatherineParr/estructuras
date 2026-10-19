#el diccionario se crea con valores por pares (clave-valor) clave y el valor delimitafos por llaves 

inventario = {"manzanas":50, "peras":30, "naranjas":100}
frutas = []

#recorresrlo
for fruta, cantidad in inventario.items():
    print(f"{fruta}: {cantidad}")
#crear una lista solo con las claves
    frutas.append(fruta)
print(frutas)












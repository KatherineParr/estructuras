from elfo import Elfo
from hombre import Hombre

def cargar_personajes(ruta_fichero: "Personajes.txt"):
    lista_elfos = []
    lista_hombres = []
    fichero = None  # Inicializamos a None para poder verificarlo en el finally

    try:
        fichero = open(ruta_fichero, mode="r", encoding="utf-8")
        
        for num_linea, linea in enumerate(fichero, start=1):
            linea_limpia = linea.strip()
            if not linea_limpia:
                continue  # Saltar líneas en blanco

            # Dividimos por coma y limpiamos espacios sobrantes en cada campo
            datos = [campo.strip() for campo in linea_limpia.split(",")]

            if len(datos) != 5:
                print(f"[AVISO] Línea {num_linea} ignorada: formato incorrecto.")
                continue

            try:
                nombre = datos[0]
                nivel = int(datos[1])
                altura = float(datos[2])
                atributo_especifico = datos[3]
                naturaleza = datos[4].lower()

                if naturaleza == "inmortal":
                    elfo = Elfo(nombre, nivel, altura, atributo_especifico)
                    lista_elfos.append(elfo)
                elif naturaleza == "mortal":
                    edad = int(atributo_especifico)
                    hombre = Hombre(nombre, nivel, altura, edad)
                    lista_hombres.append(hombre)
                else:
                    print(f"[AVISO] Línea {num_linea}: naturaleza '{naturaleza}' desconocida.")

            except ValueError as e:
                print(f"[ERROR DE DATOS] Línea {num_linea} corrupta ({e}). Se omite el registro.")

    except FileNotFoundError:
        print(f"[ERROR CRÍTICO] No se encontró el archivo '{ruta_fichero}'.")
    except OSError as e:
        print(f"[ERROR DE E/S] Problema al leer el archivo: {e}")
    finally:
        # Cierre explícito y seguro del recurso
        if fichero is not None and not fichero.closed:
            fichero.close()
            print("\n[INFO] Fichero cerrado correctamente en el bloque finally.\n")

    return lista_elfos, lista_hombres


if __name__ == "__main__":
    elfos, hombres = cargar_personajes("Personajes.txt")

    print("Lista de Elfos por orden de inserción:")
    for elfo in elfos:
        print(f"  - {elfo}")

    print("\nLista de Hombres por orden de inserción:")
    for hombre in hombres:
        print(f"  - {hombre}")

    # Prueba de métodos heredados y polimorfismo
    print("\n--- Prueba de métodos de clase ---")
    todos_los_personajes = elfos + hombres

    todos_los_personajes = elfos + hombres

    if not todos_los_personajes:
        print("No hay personajes disponibles para mostrar.")
    else:
        for personaje in todos_los_personajes:
            print(personaje.subir_nivel())
            print(personaje)

    # Si quiero subir de nivel al primer elfo y el primer hombre, todos_los_personajes:

    print("\n--- Prueba de polimorfismo con todos los personajes ---")
    
    elfo_actualizado = False
    hombre_actualizado = False

    for personaje in todos_los_personajes:
        if isinstance(personaje, Elfo) and not elfo_actualizado:
            print(personaje.subir_nivel())
            print(personaje)
            elfo_actualizado = True
            
        elif isinstance(personaje, Hombre) and not hombre_actualizado:
            print(personaje.subir_nivel())
            print(personaje)
            hombre_actualizado = True

        # Optimización: si ya encontramos y actualizamos a ambos, salimos del bucle
        if elfo_actualizado and hombre_actualizado:
            break
   
   
   

                            
                   
                            
                   
                            
                   
                            
                   
                            
                   
                            
                   
                            
                   
                            

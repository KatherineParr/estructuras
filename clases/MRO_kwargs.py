class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
class Humano:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)

class Robot:
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")

class Cyborg(Humano, Robot):
    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        print(f"[Cyborg] Iniciando directiva principal...")
        
        print("\n--- Ejecución vía super() (MRO) ---")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)
        
        print("\n--- Ejecuciones Explícitas Aisladas ---")
        Humano.ejecutar_tarea(self, tarea, prioridad) 
        Robot.ejecutar_tarea(self, tarea, prioridad)

terminator = Cyborg()
terminator.ejecutar_tarea("Proteger a John Connor", 1)

print("\n--- Cadena MRO de la clase Cyborg ---")
print([cls.__name__ for cls in Cyborg.mro()])
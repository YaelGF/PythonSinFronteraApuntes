
# Escribir una funcion que indique si el usuario es mayor de edad

# Mia
def ine(edad:int) -> str:
    return "mayor de edad" if edad >= 18 else "menor de edad" 

print(ine(5))
print(ine(18))
print(ine(20))

# Holamundo

def esMayor(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self, edad):
        self.edad = edad

usuario = Usuario(15)
usuario2 = Usuario(25)

resultado1 = esMayor(usuario)
resultado2 = esMayor(usuario2)

print(resultado1, resultado2)


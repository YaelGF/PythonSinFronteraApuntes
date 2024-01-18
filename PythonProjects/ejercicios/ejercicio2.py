
# Ingresar nombre y apellido e imprimirlo al reves

def invertir(name:str, lastname:str) -> str:
    name = name[::-1]
    lastname = lastname[::-1]
    return name + " " + lastname


n = input("ingresa tu nombre: ")
a = input("ingresa tu apellido: ")

print(invertir(n,a)) 

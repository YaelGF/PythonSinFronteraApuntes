from telnetlib import GA


class Animales:
    def __init__(self,nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludos(self):
        print("Hola mi nombre es", self.nombre)

class Gato(Animales):
    def maullar(self):
        print(self.onomatopeya)

class Perro(Animales):
    def auyar(self):
        print(self.onomatopeya)

class Pajaro(Animales):
    def birriar(self):
        print(self.onomatopeya)


gato = Gato("Felipe","Miau")
perro = Perro("Loky","Guau")
pajaro = Pajaro("Piolin", "FIU")

gato.saludos()
gato.maullar()

perro.saludos()
perro.auyar()

pajaro.saludos()
pajaro.birriar()
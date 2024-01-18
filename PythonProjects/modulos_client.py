from modulos import saludo, mascotas
from camelcase import CamelCase

print(mascotas)

saludo("yael")

c = CamelCase()
s = "esta oracion necesita CamelCase!"

camelcased = c.hump(s)
print(camelcased)

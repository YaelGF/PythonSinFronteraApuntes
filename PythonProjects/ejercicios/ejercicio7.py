# Escribir una funcion que indique cuantas vocales tiene una palabra

str = "HolA"
count = 0
for i in str:
    i = i.lower()
    count += 1 if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' else 0
print(count)
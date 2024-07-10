# Escribir una aplicación que reciba una cantidad infinita de numeros hasta
# decir basta, luego que devuelva la suma de los numeros ingresados

nums =[]
print("Ingrese numeros y para salir escriba basta")
while(True):
    num = input("Ingrese numero: ")
    if num == "basta":
        break
    else:
        try:
            nums.append(int(num))
        except:
            print("Dato invalido")
            exit()
result = 0
for i in nums:
    result += i
print(result)
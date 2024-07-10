# Escribir una función que indique si un número es par o impar

def par_impar(num:int) -> str:
    return "par" if (num % 2) == 0  else "impar" 

print(par_impar(2))
print(par_impar(5))
print(par_impar(222))
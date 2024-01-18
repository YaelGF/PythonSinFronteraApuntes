
# Multiplicar dos numeros sin usar el simbolo de multiplicacion

def multiplicacion(num1:int, num2:int) -> int:
    result = 0
    for i in range(num2):
        result += num1
    return result

print(multiplicacion(2,5))

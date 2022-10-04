
primernumero = input('Ingrese primer número: ')

try:
    primero = int(primernumero)
except:
    primero = "Error"

if primero == "Error":
    print("El valor ingresado no es un entero")
    exit()

segundonumero = input('Ingrese segundo número: ')

try:
    segundo = int(segundonumero)
except:
    segundo = "Error"

if segundo == "Error":
    print('El valor ingresado no es un entero')
    exit()

simbolo = input("Ingrese operación: ")

if simbolo == '+':
    print('Suma: ', primero + segundo)
elif simbolo == '-':
    print('Resta: ', primero - segundo)
elif simbolo == '*':
    print('Multiplicación: ', primero * segundo)
elif simbolo == '/':
    print('División: ', primero / segundo)
else:
    print('El simbolo ingresado no es válido')


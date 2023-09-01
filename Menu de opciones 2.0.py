'''Binario a decimal, decimal a binario y Operaciones basicas eb python (+-*/)
Menu de opciones'''
def binario_a_decimal(binario):
    return int(binario, 2)

def decimal_a_binario(decimal):
    return bin(decimal)[2:]

def M(a, b):
    return a * b

def D(a, b):
    return a / b

def S(a, b):
    return a + b

def R(a, b):
    return a - b

while True:
    print("*** Menu principal ***")
    print("1. Convertir de binario a decimal")
    print("2. Convertir de decimal a binario")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sumar")
    print("6. Restar")
    print("7. Salir")

    opcion = input("Ingrese una opcion")
    
    if opcion == '1':
        binario = input("ingresa un numero binario: ")
        decimal = binario_a_decimal(binario)
        print(f"El equivalente decimal es: {decimal}")

    elif opcion == '2':
        decimal = int(input("ingresa un numero decimal: "))
        binario = decimal_a_binario(decimal)
        print(f"El equivalente binario es: {binario}")

    elif opcion == '3':
        a = float(input("ingresar un primer numero: "))
        b = float(input("Ingresa un segundo numero: "))
        print("La multiplicacion es: ",M(a, b))
        
    elif opcion == '4':
        c = float(input("ingresar un primer numero: "))
        d = float(input("Ingresa un segundo numero: "))
        print("La devision es: ",D(c, d))    

    elif opcion == '5':
        e = float(input("ingresar un primer numero: "))
        f = float(input("Ingresa un segundo numero: "))
        print("La suma es: ",S(e, f)) 

    elif opcion == '6':
        g = float(input("ingresar un primer numero: "))
        h = float(input("Ingresa un segundo numero: "))
        print("La resta es: ",R(g, h))

    elif opcion == '7':
        print("Saliendo del programa...")
        break
    
# 1. Hacer un programa que calcule independientemente la suma de los pares y los impares de los números entre 1 y 1000.

# Solución 1
sumaPar = 0
sumaImpar = 0

for i in range(1, 1001):
    if (i % 2) == 0:
        sumaPar = sumaPar + i
    else:
        sumaImpar = sumaImpar + i

print(
    f"La suma de los números pares es: {sumaPar}. Y la suma de los números impares es: {sumaImpar}")

# Solución 1.2
contador = 0
contadorimpar = 0
for x in range(1, 1001):

    if x % 2 == 0:
        contador += x
    else:
        contadorimpar += x

print(f"la suma de numeros pares es {contador}, e impares {contadorimpar}")


# 2. Realizar la tabla de multiplicar de un número entre 0 y 10.

print("Programa para mostrar la tabla de multiplicar de un número del 1 al 10")

def tablaMultiplicar(numero):
    for i in range(11):
        multiplicacion = numero * i
        print(f"{numero} * {i} = {multiplicacion}")


numero = int(input("Digite un numero: "))
tablaMultiplicar(numero)


# 3. Imprimir y contar los múltiplos de 3 desde la unidad hasta un número que introducimos por teclado.

# Solucion 3.1
num = int(input("Ingrese un número "))
cont = 0

for i in range(1, num+1):
    if i % 3 == 0:
        cont+=1

print(f"La cantidad de números múltiplos de 3 en el rango 1 - {num} es: {cont}")

# Solucion 3.2
contador = 0
numero = int(input("inserte numero:"))

for z in range(1, numero + 1):

    if(z % 3 == 0):
        contador += 1
        print(z)

print(contador)

# 4. Suponga que un individuo desea invertir su capital en un banco y desea saber cuánto dinero ganara después de (cantidad de meses dada por teclado) si el banco paga a razón de 2% mensual.

#Solucion 4.1
capital = int(input("inserte capital: "))
meses = int(input("inserte meses: "))
porc = 0.02
contador = 0

for s in range (1,meses+1):
    # print (s)
    contador += (capital*porc)

print(f"capital total en los {meses} meses, se obtuvo de {capital} capital inicial, a un total de {contador+capital} ")

#Solucion 4.2
capital = int(input("Ingrese el capital "))
numMeses = int(input(
    "Por cuánto tiempo (en meses) le gustaría invertir su dinero en nuestro? "))
capInicial = capital
intereses = 0

for i in range(1, numMeses+1):
    intereses = intereses + capital*0.02
    capital = capital + intereses

print(
    f"La ganancia obtenida en {numMeses} meses por un capital invertido de {capInicial} es de {intereses}")


# 5. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.

#Solucion 5.1
print("Programa para calcular el total de compra con descuento por producto")

def totalPagar():
    cantidadProductos = int(input("Digite la cantidad de productos: "))
    totalPago = 0
    subtotal = 0
    for i in range(1, cantidadProductos+1):
        valorProducto = int(input("Digite el valor del producto: "))
        subtotal = valorProducto - (valorProducto * 0.15)
        totalPago += subtotal
    return totalPago

print(totalPagar())

#Solucion 5.2
print("***TIENDA VIRTUAL***")

subtotal = 0

menu = int(input("inserte el valor de la compra, si desea finalizar digite 0 "))

while (menu != 0):
    subtotal += menu
    menu = int(
        input("inserte el valor de la compra, si desea finalizar digite 0 "))
else:
    descuento = subtotal * 0.15
    total = subtotal - descuento
    print(f"total de pago {total}")

#Solucion 5.3 la de profe

compra = [10000, 4000, 2000]
total = 0

for indice in range(len(compra)):
    subtotal = compra[indice] - (compra[indice] * 0.15)
    total += subtotal

print(f"total es {total}")

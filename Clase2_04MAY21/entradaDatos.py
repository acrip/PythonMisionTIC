nombre = input("Escribe tu nombre: ")
print(f"Hola {nombre}")
x = int(input("Escribe el valor de x: "))
print(f"X vale {x}")
print(f"x + 3 = {x + 3}")

# Se solicita calcular el area y el perimetro de un rectangulo 
# solicitando los valores por teclado e imprimir los resultaods por consola

ancho = int(input("Escribe el ancho del rectangulo: "))
alto = int(input("Escribe el alto del rectangulo: "))

area = ancho * alto
perimetro = (ancho + alto) * 2

print("El area del rectangulo es: " + str(area))
print("El perimetro del rectangulo es: " + str(perimetro))

# Solicitar por teclado dos valores y determinar cual es el mayor

num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el segundo numero: "))

if(num1 > num2):
    print("el numero " + str(num1) + " es el mayor")
else:
    print("el numero " + str(num2) + " es el mayor")
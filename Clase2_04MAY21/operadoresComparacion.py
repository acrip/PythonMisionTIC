a = 2
b = 2
resultado = a == b
print(resultado)

cad1 = "Cadena"
cad2 = "cadena"
resul = cad1 == cad2
print(resul)

mayor = a > b
print(f"Mayor que: {mayor}")

menor = a < b
print(menor)

diferente = cad1 != cad2
print(diferente)

mayorIgual = a >= b
print(f"Mayor igual que: {mayorIgual}")

menorIgual = a <= b
print(f"Menor igual que: {menorIgual}")

if a % 2 == 0:
    print("Es par")
else:
    print("Es impar")

edadLimite = 18
edadPersona = 16

if(edadPersona >= edadLimite):
    print("Es mayor de edad")
else:
    print("Es menor de edad")
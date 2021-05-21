#1.  Diseñar un programa que lea el valor correspondiente a una distancia en millas
#    marinas y las escriba expresadas en metros. Sabiendo que 1 milla marina equivale datetime a 
#    1852 metros.
#    
millas = int(input("Escribe la cantidad de millas a convertir: "))
metros = millas * 1852
print(f"{millas} millas son {metros} metros")

#2.  Diseñar un programa que escribe el porcentaje descontado por una compra,
#    introducinedo por teclado el precio de la venta y el valor pagado.
#    
precioVenta = int(input("Ingrese el precio de venta: "))
valorPagado = int(input("Ingrese el valor pagado: "))

descuento = int(100-(valorPagado * 100 / precioVenta))
print(f"Para un precio de venta de {precioVenta} y un valor pagado de {valorPagado} el descuento fue del {descuento}%")

#3.  Diseñar un programa que tras introducir una medida expresada en centimetros la
#    convierta en pulgadas (1 pulgada es 2.54 centimetros).
#    

centimetro = int(input("Ingrese los centimetros a convertir: "))
pulgada = 2.54

print(f"{centimetro} centimetros son {centimetro / pulgada} pulgadas.")

#4.  Diseñar un programa que exprese en horas, minutos y segundos un tiempo expresado en
#    segundos.
#    
totalSegundos = int(input("Ingrese la cantidad de segundos a convertir: "))
horas = totalSegundos // 3600
totalSegundos = totalSegundos % 3600
minutos = totalSegundos // 60
totalSegundos %= 60
print(f"El tiempo es de {horas} horas, {minutos} minutos, {totalSegundos} segundos.")

#5.  realizar un algoritmo que me permita ingresar la hora, minutos y segundos y que me
#    indique cuantos segundos son.

horas = int(input("Ingrese la cantidad de horas: "))
minutos = int(input("Ingrese la cantidad de minutos: "))
segundos = int(input("Ingrese la cantidad de segundos: "))
totalSegundos = (horas * 3600) + (minutos * 60) + segundos

print(f"El total de segundos es: {totalSegundos} segundos.")
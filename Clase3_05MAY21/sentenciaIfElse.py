#if condicion:
#    accion a ejecutar
#else:
#    accion a ejecutar
##***************************
#
#if condicion:
#    accion a ejecutar
##***************************
#
#if condicion:
#    accion a ejecutar
#elif condicion2:
#    accion a ejecutar
#elif condicion3:
#        accion a ejecutar
#else:
#    accion a ejecutar
##***************************

#numero = int(input("Ingrese un numero: "))
#
#if numero <= 5:
#    texto = "El numero es menor que 5"
#elif numero > 5 & numero <= 10:
#    texto = "El numero esta entre 5 y 10"
#elif numero > 10:
#    texto = "El numero es mayor a 10"
#else:
#    texto = "No se puede determinar un rango para el numero"
#    
#print(texto) 
#    
#numero = 45
#numero2 = 23
#
#if numero > 5:
#    if numero2 < 10:
#        texto = "ok, se cumplen"
#    elif numero2 < 50:
#        texto = "Si es menor que 50"
#    else:
#        texto = "NO pas el numero2"
#elif numero ==5:
#    texto = "Es igual a 5"
#    
#mes = int(input("Ingrese un numero entre 1 y 12 para el mes: "))   
#if mes > 0 and mes < 3:
#    print("Invierno")
#elif mes > 2 and mes < 7:
#    print("Primavera")
#elif mes > 6 and mes < 10:
#    print("Verano")
#elif mes > 9 and mes < 13:
#    print("Otoño")
#else:
#    print("El numero ingresado no corresponde a un mes del año")
    
    
# 1.    Crear un sistema de calificaciones segun se solicita.
#       El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
#       El usuario proporcionara un valor entre 0 y 10

#       Si estan entre 9 y 10: imprimir una A
#       Si estan entre 8 y menor a 9: imprimir una B
#       Si estan entre 7 y menor a 8: imprimir una C  
#       Si estan entre 6 y menor a 7: imprimir una D   
#       Si estan entre 0 y menor a 6: imprimir una F

#       Cualquier otro valor debe imprimir: valor desconocido     

valor = int(input("ingrese una valor entre 1 y 10: "))
if(valor > 0 and valor < 6):
    print("Calificacion : F")
elif(valor == 6):
    print("Calificacion : D")
elif(valor == 7):
    print("Calificacion : C")
elif(valor == 8):
    print("Calificacion : B")
elif(valor > 8 and valor < 11):
    print("Calificacion : A")
else:
    print("Valor desconocido.")
    
    
#2. Dada la duracion en minutos de una llamada calcular el costo, considerando
#   -Hasta tres minutos el costo es de 200
#   -Por encima de tres minutos el costo es de 200 mas 50 por cada minutos adicional a los tres primeros

#3. Dado el monto se una compra calcular el descuento considerando
#   -Descuento es 10% si el monto es mayor a 10000 pesos
#   -Descuento es 20% si el monto es mahor a 5000 pesos y menor o igual a 10000 pesos
#   -No hay descuento si el monto es menor o igual a 5000


#TODO: Falta completar estos ejercicios, no deberian suponer ninguna complejidad



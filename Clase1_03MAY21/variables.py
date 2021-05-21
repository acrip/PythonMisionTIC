# Case sensitive Significa que el uso de mayusculas y minusculas 
# afecta el nombre de las variables
#variable_numerica   #Snake Case
#VariableNumerica  #Camel Case
#variableNumerica  #Camel Case

x = 5
y = 3
z = x + y
print(f"La suma es: {z}") #Se usa para formatear todo el texto a string
print("La suma es: "+ str(z)) #Se utiliza para convertir variable numericas a string y asi poder concatenar
print(z)
print(type(z)) #Imprime el tipo de dato de una variable
varResta = x - y
print("La resta es: "+ str(varResta))
varMulti = x * y
print("La multiplicacion es: "+ str(varMulti))
varDivFlot = x / y   #Para imprimir usando flotantes
print("La division flotante es: "+ str(varDivFlot))
varDivInt = x // y   #Para imprimir usando solo parte entera
print("La division entera es: "+ str(varDivInt))
varMod = x % y  #Retorna el residuo de una division
print("El modulo es: "+ str(varMod))
varExp = x ** y #La clásica función potencia: un número a elevado a un número b
print("El exponente es: "+ str(varExp ))

resultado = varMulti - (x / y)
print("el resultado es: "+ str(resultado))

x = 43
x = x + 1
print("El nuevo valor de x es: " + str(x))

lado = 38
perimeroCuadrado = lado * 4
areaCuadrado = lado*lado

print("El perimetro del cuadrado es: " + str(perimeroCuadrado))
print("El area del cuadrado es: " + str(areaCuadrado))

a = 3.5
print(a)
print(type(a))

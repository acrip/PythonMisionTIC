nombre = "Andres Zapata"
letra = 'a'

print(nombre + " Estudiante")
print (len(nombre))
print(nombre.upper())
print(nombre.lower())
print(nombre.lower().title())
print(nombre.swapcase())
print(nombre.capitalize())
print(nombre.replace("e","é"))
print(nombre.count('a'))
contador = nombre.count('a')
print(contador)
print(nombre.startswith('A'))
nombreEspacios = "      " + nombre + "       "
print(nombreEspacios)
print(nombreEspacios.strip()) 
print(nombre.find('s'))
print(nombre.find('a', 8))
print(nombre[2])
print(nombre[-4])
print(nombre[0:4])
print(nombre[5:10])
print(nombre[5:5])
print(nombre[:5])
print(nombre[5:])
print(nombre[:])

nuevoNombre = 'C' + nombre[1:]
print(nuevoNombre)

if('oas' in nombre) : 
    print("OK")
else:
    print("NO")
    
print(nombre + "\nEs un estudiante")

saludo = "Hola" * 3
print (saludo + nombre)

otroNombre = "Carlos"
otroNombre += " y "
otroNombre += "Camila"
print(otroNombre)
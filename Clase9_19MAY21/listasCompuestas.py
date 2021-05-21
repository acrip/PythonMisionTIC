#listaCompuesta = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

#print(listaCompuesta)
#print(listaCompuesta[0])
#print(listaCompuesta[0][0])
#print(listaCompuesta[2][2])
#print()
#for i in range(len(listaCompuesta[0])):
#    print(listaCompuesta[0][i])
    
#for i in range(len(listaCompuesta)):
#    for j in range(len(listaCompuesta[i])):
#        print(listaCompuesta[i][j])
#    print()
    
# 1. Crear una lista con 2 elementos, cada elemento será una lista de 5 enteros, 
# calcular y mostrar la suma de los elementos
#listaEnteros = [[1,2,3,4,5],[6,7,8,9,10]]
#suma = 0
#for i in range(len(listaEnteros)):
#    for j in range(len(listaEnteros[i])):
#        suma += listaEnteros[i][j]
#
#print(suma)

# 2. Definir 2 listas de 3 elementos (Todos los valores ingresados por teclado)
#    - En la primera lista cada elemento tendrá como sublista, el nombre del padre y la madre de una familia.
#    - La segunda lista tendrá sublistas con nombres de los hijos de cada familia, pueden haber familias sin hijos.
#    - Imprimir los nombres del padre, la madre y sus hijos.

listaPadres = []
listaHijos = []

for i in range(3):
    listaPadres.append([input("Ingrese el nombre del padre de la familia " + str(i + 1))], [input("Ingrese el nombre de la madre de la familia " + str(i))])
    cantidadHijos = input("Ingrese la cantidad de hijos de la familia " + str(i + 1))
    for j in range(cantidadHijos):
        listaHijos[i].append(input("Ingrese el hijo "+ str(j + 1)+" para la familia" + str(i + 1)))

print(listaPadres)
print(listaHijos) 

    
#listaPadres = [["juan", "maria"], ["carlos", "sandra"], ["felipe", "isabela"]]
#listaHijos = [["Sebastian, Camila"], [], ["Cristian"]]
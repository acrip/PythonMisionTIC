listaPadres = []
listaHijos = []

for i in range(3):
    listaPadres.append([[input("Ingrese el nombre del padre de la familia " + str(i + 1)+": ")], [input("Ingrese el nombre de la madre de la familia " + str(i + 1)+": ")]])
    cantidadHijos = input("Ingrese la cantidad de hijos de la familia " + str(i + 1))
    for j in range(cantidadHijos):
        listaHijos[i].append(input("Ingrese el hijo "+ str(j + 1)+" para la familia " + str(i + 1) + ": "))

print(listaPadres)
print(listaHijos) 